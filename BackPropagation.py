import numpy as np
import random

def forward(NumberOfLayers,row, weights,bias):
    for i in range(NumberOfLayers + 1):
     weight = np.array(weights[i])
     result = weight.dot(row)
     #7zawed el bias lel next iteration
     row=np.insert(result, 0, bias, axis=0)
    return result


def create_array(m, n):
    arr = []
    for i in range(m):
        col = []
        for j in range(n):
            col.append(random.uniform(-1, 1))

        arr.append(col)

    return arr


def initialize_weights(NumberOfLayers,neurons,numberOfFeatures):
    ind = 0
    m = neurons[ind]
    n = numberOfFeatures+1
    weights = []
    for i in range(NumberOfLayers + 1):
        arr = create_array(m, n)
        weights.append(arr)
        if(i==NumberOfLayers):
            break
        ind = ind + 1;
        m = neurons[ind];
        n = neurons[ind-1]+1;

    return weights

def Train(trainX, TrainY, l_rate, n_epoch,NumberOfLayers,neurons,numberOfFeatures,bias):
    trainX = np.array(trainX)
    weights = initialize_weights(NumberOfLayers,neurons,numberOfFeatures)
    for epoch in range(n_epoch):
        for i, row in enumerate(trainX):
            F = forward(NumberOfLayers,row, weights,bias)
            print(F)
    return weights
