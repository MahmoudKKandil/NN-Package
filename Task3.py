
import pandas as pd
import Form3
import Pre3
iris = pd.read_csv("Iris.csv")
df = pd.DataFrame(iris)
NumberOfLayers, NumberOfNerons, LearningRate, epochs,bias,chosenFunct=Form3.Task3MainForm()
LearningRate = float(LearningRate)
Epochs = int(epochs)
bias = int(bias)
NumberOfLayers = int(NumberOfLayers)
NumberOfNeron=[]
for i in NumberOfNerons.split(','):
    NumberOfNeron.append(int(i))

data_train,data_test = Pre3.Encode(iris.iloc[:,1: 6],bias)
Target=Pre3.Encode3(data_train)

