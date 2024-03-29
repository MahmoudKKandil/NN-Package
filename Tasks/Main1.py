import numpy as np
import Pre
import ConfusionMatrix
import matplotlib.pyplot as plt
import adaline
import pandas as pd


def MainFunc(chosenF1, chosenF2, chosenC1, chosenC2, LearningRate, Epochs, bias, threshold, df):
    LearningRate = float(LearningRate)
    Epochs = int(Epochs)
    threshold = float(threshold)

    data_train, data_test, data_trainNotShuffled = Pre.Encode(df, chosenC1, chosenC2, chosenF1, chosenF2, bias)
    Y_train = Pre.Encode2(data_train, chosenC1)
    Y_test = Pre.Encode2(data_test, chosenC1)

    weights = adaline.train_weights(data_train.iloc[:, 0:3], Y_train, LearningRate, Epochs, threshold)

    accuracy, trueP, FalseP, FalseNeg, trueNeg = adaline.test_Data(data_test.iloc[:, 0:3], Y_test, weights)

    class1 = plt.scatter(data_trainNotShuffled.iloc[:30, 1], data_trainNotShuffled.iloc[:30, 2], color='hotpink')
    class2 = plt.scatter(data_trainNotShuffled.iloc[30:60, 1], data_trainNotShuffled.iloc[30:60, 2], color='blue')
    plt.legend((class1, class2),
               (chosenC1, chosenC2),
               scatterpoints=1,
               loc='upper left',
               fontsize=6)
    maxValue = df[chosenF1].max()
    x = np.array([0, abs(maxValue)])
    plt.plot(x, ((-1 * weights[1] * x) - weights[0]) / weights[2])
    plt.show()
    ConfusionMatrix.DrawMatrix(trueP, FalseP, FalseNeg, trueNeg)
    return accuracy