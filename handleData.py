import csv
import random

def loadDataset(filename, split, trainingSet[], testSet[]):
    with open(filename, 'rb') as csvfile:
        line = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(len(dataset)-1):
            for y in range(4):
                dataset[x][y] = float(dataset[x][y])

