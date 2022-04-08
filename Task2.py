import numpy as np
import Perceptron
import pandas as pd
import Plotter
import Form
import Pre
import ConfusionMatrix
import matplotlib.pyplot as plt
import adaline
import form2

iris = pd.read_csv("Iris.csv")
df = pd.DataFrame(iris)
Plotter.DrawIris(iris)
chosenF1, chosenF2, chosenC1, chosenC2, LearningRate, Epochs, bias, threshold = form2.Task2MainForm()
LearningRate = float(LearningRate)
Epochs = int(Epochs)
threshold = float(threshold)
data_train, data_test, data_trainNotShuffled = Pre.Encode(df, chosenC1, chosenC2, chosenF1, chosenF2, bias)
Y_train = Pre.Encode2(data_train, chosenC1)
Y_test = Pre.Encode2(data_test, chosenC1)
weights = adaline.train_weights(data_train.iloc[:, 0:3], Y_train, LearningRate, Epochs, threshold)
accuracy, trueP, FalseP, FalseNeg, trueNeg = Perceptron.test_Data(data_test.iloc[:, 0:3], Y_test, weights)

print("Accuracy: ", accuracy)
ConfusionMatrix.DrawMatrix(trueP, FalseP, FalseNeg, trueNeg)
