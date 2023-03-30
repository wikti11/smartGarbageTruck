# Intelligent Garbage Truck

## Premise

The goal of this project was to create an intelligent garbage truck that collects trash from bins which are left by residents, it then segregates them on its own and transports them to the landfill.

## Specifications

The garbage truck moves around randomly generated map using A* algorithm. It recognizes garbage type using neural network algorithms (with also availability of using decision trees or generic algorithm instead). Each tile has different cost to determin the quickest route to the destination. The garbage truck collects garbage from every bin that is not empty and then it transports sorted garbage to the landfill.

## Additional information

This project was created by a group of 4 people using Python (sklearn, torch, pygame). It was developed from March until June 2022. 