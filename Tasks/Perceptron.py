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

def test_Data(testX, testY, weights):
    testX = np.array(testX)
    weights = np.array(weights)

    correct=0
    trueP=0
    trueNeg=0
    FalseP=0
    FalseNeg=0
    for i, row in enumerate (testX):
        predtected = predict(row,weights)
        #truePositive/TrueNeg
        if predtected == testY[i]:
            correct+=1
            if predtected==1:
                trueP+=1
            else:
                trueNeg+=1
        #FalsePositive/FalseNegative
        if predtected != testY[i]:
            if predtected==1:
                FalseP+=1
            else:
                FalseNeg+=1

    accuracy = (correct/len(testX))*100
    return accuracy,trueP,FalseP,FalseNeg,trueNeg
