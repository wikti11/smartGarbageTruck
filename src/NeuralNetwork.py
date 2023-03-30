import torch
from torch import nn
from torch import optim
from torch.utils.data import DataLoader
from torchvision import datasets, transforms, models
import os.path
from collections import OrderedDict
from PIL import Image
import numpy as np


class NeuralNetwork:

    def __init__(self):
        self.model = None
        self.trainTransforms = None
        self.trainDataset = None
        self.trainLoader = None
        self.criterion = None
        self.optimizer = None

    def createNewModel(self):
        print("Creating new model...")
        self.trainTransforms = transforms.Compose([transforms.RandomRotation(30),
                                                   transforms.RandomResizedCrop(224),
                                                   transforms.RandomHorizontalFlip(),
                                                   transforms.ToTensor(),
                                                   transforms.Normalize([0.485, 0.456, 0.406],
                                                                        [0.229, 0.224, 0.225])])

        self.trainDataset = datasets.ImageFolder(os.path.join("..", "resources", "nn"),
                                                 transform=self.trainTransforms)

        self.trainLoader = DataLoader(self.trainDataset, batch_size=32, shuffle=True)

        self.model = models.vgg16(pretrained=True)

        for parameter in self.model.parameters():
            parameter.requires_grad = False

        self.classifier = nn.Sequential(OrderedDict([('fc1', nn.Linear(25088, 500)),
                                                     ('relu', nn.ReLU()),
                                                     ('drop', nn.Dropout(p=0.5)),
                                                     ('fc2', nn.Linear(500, 5)),
                                                     ('output', nn.LogSoftmax(dim=1))]))

        self.model.classifier = self.classifier

        self.criterion = nn.NLLLoss()

        self.optimizer = optim.Adam(self.model.classifier.parameters(), lr=0.001)

        print("Created new model")

    def trainClassifier(self):
        print("Training model...")
        epochs = 15
        steps = 0
        printEvery = 10
        self.model.to('cuda')

        for e in range(epochs):

            self.model.train()
            runningLoss = 0

            for images, labels in iter(self.trainLoader):

                steps += 1
                images, labels = images.to('cuda'), labels.to('cuda')
                self.optimizer.zero_grad()
                output = self.model.forward(images)
                loss = self.criterion(output, labels)
                loss.backward()
                self.optimizer.step()
                runningLoss += float(loss.item())

                if steps % printEvery == 0:
                    self.model.eval()

                    print("Epoch: {}/{}.. ".format(e + 1, epochs),
                          "Training Loss: {:.3f}.. ".format(runningLoss / printEvery))

                    runningLoss = 0
                    self.model.train()
        print("Trained model")

    def saveCheckpoint(self):
        print("Saving checkpoint...")
        self.model.class_to_idx = self.trainDataset.class_to_idx

        checkpoint = {'arch': "vgg16",
                      'class_to_idx': self.model.class_to_idx,
                      'model_state_dict': self.model.state_dict()
                      }

        torch.save(checkpoint, 'checkpoint.pth')
        print("Saved checkpoint")

    def loadCheckpoint(self):
        print("Loading checkpoint...")
        checkpoint = torch.load("checkpoint.pth")

        if checkpoint['arch'] == 'vgg16':

            self.model = models.vgg16(pretrained=True)

            for param in self.model.parameters():
                param.requires_grad = False
        else:
            print("Architecture not recognized.")

        self.model.class_to_idx = checkpoint['class_to_idx']

        self.criterion = nn.Sequential(OrderedDict([('fc1', nn.Linear(25088, 500)),
                                                    ('relu', nn.ReLU()),
                                                    ('drop', nn.Dropout(p=0.5)),
                                                    ('fc2', nn.Linear(500, 5)),
                                                    ('output', nn.LogSoftmax(dim=1))]))

        self.model.classifier = self.criterion

        self.model.load_state_dict(checkpoint['model_state_dict'])

        print("Loaded checkpoint")

    def processImage(self, imagePath):
        #print("Processing image...")
        pilImage = Image.open(imagePath)

        if pilImage.size[0] > pilImage.size[1]:
            pilImage.thumbnail((5000, 256))
        else:
            pilImage.thumbnail((256, 5000))

        leftMargin = (pilImage.width - 224) / 2
        bottomMargin = (pilImage.height - 224) / 2
        rightMargin = leftMargin + 224
        topMargin = bottomMargin + 224

        pilImage = pilImage.crop((leftMargin, bottomMargin, rightMargin, topMargin))
        npImage = np.array(pilImage) / 255
        mean = np.array([0.485, 0.456, 0.406])
        std = np.array([0.229, 0.224, 0.225])
        npImage = (npImage - mean) / std
        npImage = npImage.transpose((2, 0, 1))

        #print("Processed image")
        return npImage

    def predict(self, image):
        print("Predicting...")
        image = torch.from_numpy(image).type(torch.FloatTensor)
        image = image.unsqueeze(0)

        output = self.model.forward(image)
        allProbabilities = torch.exp(output)

        topProbabilities, topIndices = allProbabilities.topk(2)
        topProbabilities = topProbabilities.detach().type(torch.FloatTensor).numpy().tolist()[0]
        topIndices = topIndices.detach().type(torch.FloatTensor).numpy().tolist()[0]
        idxToClass = {value: key for key, value in self.model.class_to_idx.items()}
        topClasses = [idxToClass[index] for index in topIndices]

        #print("Predicted")
        return topProbabilities, topClasses

    def classifyImage(self, imagePath):
        topP, topC = self.predict(self.processImage(imagePath))
        category = ""
        if topP[0] < 0.6:
            category = "mixed"
        else:
            category = topC[0]
        print("Classified as :", category)
        return category
