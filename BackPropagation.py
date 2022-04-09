import numpy as np

def predict(row, weights):
    result = weights.T.dot(row)
    return 1.0 if result >= 0.0 else -1.0

def train_weights(trainX, TrainY, l_rate, n_epoch):
    trainX = np.array(trainX)
    weights = np.random.rand(trainX.shape[1])

    for epoch in range(n_epoch):
        for i, row in enumerate (trainX):
            prediction = predict(row, weights)
            error = TrainY[i] - prediction
            weights = weights + l_rate * error * row
    return weights
def initialize_weights(trainX, TrainY, l_rate, n_epoch):
    trainX = np.array(trainX)
    weights = np.random.rand(trainX.shape[1])

    for epoch in range(n_epoch):
        for i, row in enumerate (trainX):
            prediction = predict(row, weights)
            error = TrainY[i] - prediction
            weights = weights + l_rate * error * row
    return weights