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
chosenF1, chosenF2, chosenC1, chosenC2, LearningRate, Epochs,bias,threshold=form2.Task2MainForm()
LearningRate = float(LearningRate)
Epochs = int(Epochs)
threshold=float(threshold)
data_train,data_test,data_trainNotShuffled = Pre.Encode(df, chosenC1, chosenC2,chosenF1, chosenF2, bias)
Y_train=Pre.Encode2(data_train,chosenC1)
Y_test=Pre.Encode2(data_test,chosenC1)
weights = adaline.train_weights(data_train.iloc[:,0:3],Y_train, LearningRate, Epochs,threshold)
accuracy,trueP,FalseP,FalseNeg,trueNeg =adaline.test_Data(data_test.iloc[:,0:3],Y_test,weights)
class1=plt.scatter(data_trainNotShuffled.iloc[:30, 1], data_trainNotShuffled.iloc[:30, 2],color = 'hotpink')
class2=plt.scatter(data_trainNotShuffled.iloc[30:60, 1], data_trainNotShuffled.iloc[30:60, 2],color = 'blue')
plt.legend((class1, class2),
           (chosenC1, chosenC2),
           scatterpoints=1,
           loc='upper left',
           fontsize=6)
minValue = df[chosenF1].min()
maxValue = df[chosenF1].max()
x=np.array([minValue,maxValue])
plt.plot(x,((-1*weights[1]*x)-weights[0])/weights[2])
plt.show()
Plotter.DrawIris(df)

print("Accuracy: ",accuracy)
ConfusionMatrix.DrawMatrix(trueP,FalseP,FalseNeg,trueNeg)
