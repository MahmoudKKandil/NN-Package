from tkinter import *
from tkinter import ttk
import seaborn as sn
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import pandas as pd
import Form3
import Pre3
import BackPropagation

def Task3MainForm():
    form3 = Tk()
    form3.geometry("400x450")
    form3.resizable(False, False)
    form3.title("MLP using Backpropagation")
    ActivationFunc= ['SigmoidFunction','HyperbolicTangent']
    chosenFunc = ttk.Combobox(form3, values=ActivationFunc)
    NumOfLayersLabel = Label(form3, text="Enter number of hidden layers ")
    NumOfNeuronsLabel = Label(form3, text="Enter number of neurons(Split by , ) ")
    etaLabel = Label(form3, text="Enter Learning rate(eta)")
    epochsLabel = Label(form3, text="Enter number of epochs (m)")
    NumberOfLayersTB = Entry(form3)
    NumberOfNeronsTB  = Entry(form3)
    etaTB = Entry(form3)
    epochsTB = Entry(form3)
    var1 = IntVar()
    biasCheckbox = ttk.Checkbutton(form3, variable=var1, text='add bias?', onvalue=1, offvalue=0)
    TestAcc = Text(form3,
                  bg="light cyan", height=2,
                  width=10)
    TrainAcc = Text(form3,
                  bg="light cyan", height=2,
                  width=10)
    AccuracyLabel = Label(form3, text="Show Test Accuracy ")
    TrainAccuracyLabel = Label(form3, text="Show Train Accuracy ")
    NumOfLayersLabel.pack()
    NumberOfLayersTB.pack()
    NumOfNeuronsLabel.pack()
    NumberOfNeronsTB.pack()
    etaLabel.pack()
    etaTB.pack()
    epochsLabel.pack()
    epochsTB.pack()
    FuncLabel = Label(form3, text="Choose Activation Function")
    FuncLabel.pack()
    chosenFunc.pack()
    biasCheckbox.pack()

    def changetext():
        iris = pd.read_csv("Iris.csv")
        df = pd.DataFrame(iris)
        NumberOfLayers=NumberOfLayersTB.get()
        NumberOfNerons=NumberOfNeronsTB.get()
        LearningRate=etaTB.get()
        epochs=epochsTB.get()
        bias=var1.get()
        chosenFunct=chosenFunc.get()
        LearningRate = float(LearningRate)
        Epochs = int(epochs)
        bias = int(bias)
        NumberOfLayers = int(NumberOfLayers)
        NumberOfNeron = []
        for i in NumberOfNerons.split(','):
            NumberOfNeron.append(int(i))
        NumberOfNeron.append(3)  # outputLayer feha 3 neurons daymn

        data_train, data_test = Pre3.Encode(iris.iloc[:, 1: 6], bias)
        Target = Pre3.Encode3(data_train, 90)
        testY = Pre3.Encode3(data_test, 60)
        numberOfFeatures = 4
        weights = BackPropagation.Train(data_train.iloc[:, 0: 5], Target, LearningRate, Epochs, NumberOfLayers,
                                        NumberOfNeron, numberOfFeatures, bias, chosenFunct)


        trainaccuracy,Z,B = BackPropagation.test_Data(data_train.iloc[:, 0: 5], Target, weights, NumberOfLayers,
                                                              bias, chosenFunct)
        accuracy, Y_Actual, predY = BackPropagation.test_Data(data_test.iloc[:, 0: 5], testY, weights, NumberOfLayers,
                                                              bias, chosenFunct)
        TrainAcc.insert(END, trainaccuracy)
        TestAcc.insert(END, accuracy)
        print("Train Accuracy: ",trainaccuracy )
        print("Test Accuracy: ",accuracy)
        columns = ['SETOSA', 'VERSICOLR', 'VIRGINICA']
        cm = confusion_matrix(Y_Actual, predY, labels=columns)
        df_cm = pd.DataFrame(cm, columns, columns)
        ax = sn.heatmap(df_cm, annot=True, annot_kws={"size": 16}, square=True, cbar=False, fmt='g')
        ax.set_ylim(0, 3)
        plt.xlabel("Predicted")
        plt.ylabel("Actual")
        ax.invert_yaxis()  # optional
        plt.show()


    b = Button(form3, text="Start", command=lambda: changetext()).pack()
    TrainAccuracyLabel.pack()
    TrainAcc.pack()
    AccuracyLabel.pack()
    TestAcc.pack()

    form3.mainloop()
    return
