import pygame
import sklearn
import pandas
from sklearn.tree import DecisionTreeClassifier


from src.Entities import GarbageTruck, House
from src.Project import Project
#Decision Tree
df = pandas.read_csv('Tree.csv', sep=';', engine='python')

days = {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5, 'Saturday': 6, 'Sunday': 7}
df['Day'] = df['Day'].map(days)

seasons = {'Spring': 1, 'Summer': 2, 'Fall': 3, 'Winter': 4}
df['Season'] = df['Season'].map(seasons)

types = {'glass': 1, 'metal': 2, 'mixed': 3, 'paper': 4, 'plastic': 5, 'bio': 6}
df['Type'] = df['Type'].map(types)

d = {'YES': 1, 'NO': 0}
df['GO'] = df['GO'].map(d)

# print(df)

features = ['Day', 'Season', 'Filling', 'Type', 'Truck_filling']
X = df[features].values
y = df['GO'].values

dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)

def predict(day, season, filling, type, truck_filling):
    return dtree.predict([[days[day], seasons[season], filling, types[type], truck_filling]])[0] == 1

#
#
# print("[1] means 'YES'")
# print("[0] means 'NO'")

# Legenda:
# Filling: 0-7
# Truck_filling: 0-5
# Spring, Summer: Monday-glass, Tuesday-metal, Wednesday-bio, Thursday-mixed, Friday-paper, Saturday-plastic, Sunday-bio
# Winter, Fall: Monday-glass, Tuesday-metal, Wednesday-plastic, Thursday-bio, Friday-paper, Saturday-mixed, Sunday-plastic



# class DecisionTree:

    # def truckCapacity(self):
    #
    # def wasteCollection(self):

    #           garbage is picked up by the truck, truck has given capacity
    #                                                                (since we have 7 pieces of waste in container, would be good to have it set at 5)
    #           garbage is collected based on Game.Menu.setDay and Game.Menu.setSeason tuples
    #           garbage is collected from wasteContainers which are located at the same coords as houses
    #           garbage truck is roaming around the map until it visits every house and collects waste from it
    #           then just do that by using decision trees