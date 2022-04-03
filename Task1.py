import numpy as np
from sklearn import datasets
import Perceptron
import pandas as pd
import Plotter
import Form
import Pre
import matplotlib.pyplot as plt
###//todo preprocessing ,,,get values from form .curent for index .get for value
###//todo X values of [1,rest of data] 1 for bias ,,, Y for class c1 ==1 c2 == -1
###//todo confusion matrix implement from scratch ,,, then order all function as in slides
weights = Perceptron.train_weights([[1,5.1,3.5],[1,4.9,3],[1,4.7,3.2],[1,4.6,3.1],[1,5,3.6],[1,5.4,3.9],
                                    [1,7,3.2],[1,6.4,3.2],[1,6.9,3.1],[1,5.5,3.3],[1,6.5,2.8],[1,5.7,2.8]],
                                   [1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1], 0.1, 8)
accuracy = Perceptron.test_Data([[1,5.1,3.5],[1,4.9,3],[1,4.7,3.2],[1,4.6,3.1],[1,5,3.6],[1,5.4,3.9],
                                    [1,7,3.2],[1,6.4,3.2],[1,6.9,3.1],[1,5.5,3.3],[1,6.5,2.8],[1,5.7,2.8]],
                                   [1,1,1,1,1,1,-1,-1,-1,-1,-1,-1],weights)
x=np.array([[1,0,1],[1,1,0]])
plt.plot(x, weights.dot(x.T))
plt.show()
Iris = datasets.load_iris()
Plotter.DrawIris(Iris)

iris = pd.read_csv("Iris.csv")

Feature1, Feature2, Class1, Class2, LearningRate, Epochs = Form.Task1MainForm()
LearningRate = float(LearningRate)
Epochs = int(Epochs)

if Class1 == 'Iris-setosa' and Class2 == 'Iris-versicolor':
    NewIris = Pre.Encode(iris, 1, 2)
elif Class1 == 'Iris-versicolor' and Class2 == 'Iris-setosa':
    NewIris = Pre.Encode(iris, 1, 2)
elif Class1 == 'Iris-setosa' and Class2 == 'Iris-virginica':
    NewIris = Pre.Encode(iris, 1, 3)
elif Class1 == 'Iris-virginica' and Class2 == 'Iris-setosa':
    NewIris = Pre.Encode(iris, 1, 3)
else:
    NewIris = Pre.Encode(iris, 2, 3)

iris = Pre.Prepro(NewIris, Feature1, Feature2)

iris = iris.astype(float)
iris['Species'] = iris['Species'].astype(int)

trainIris = iris[0:30]
trainIris2 = iris[50:80]
trainIris = trainIris.append(trainIris2)
testIris = iris[30:50]
testIris2 = iris[80:100]
testIris = testIris.append(testIris2)

