from sklearn import datasets
import  Perceptron
import pandas as pd
import Plotter
import Form
import Pre

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

Perceptron.train_weights(trainIris, LearningRate, Epochs)
