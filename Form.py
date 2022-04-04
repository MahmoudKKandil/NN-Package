from tkinter import *
from tkinter import ttk


def Task1MainForm():
    Form1 = Tk()
    Form1.geometry("400x450")
    Form1.resizable(False, False)
    Form1.title("Perceptron learning algorithm")
    featuresList = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']
    F1Label = Label(Form1, text="Choose Feature 1")
    F1Label.pack()
    chosenF1 = ttk.Combobox(Form1, values=featuresList)
    chosenF1.pack()
    F2Label = Label(Form1, text="Choose Feature 2")
    F2Label.pack()
    chosenF2 = ttk.Combobox(Form1, values=[])
    chosenF2.pack()

    def fillCB2(_):
        toRemove = chosenF1.get()
        chosenF2.set('')
        secList = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']
        secList.remove(toRemove)
        chosenF2['values'] = secList
    chosenF1.bind('<<ComboboxSelected>>', fillCB2)

    Classes = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
    c1Label = Label(Form1, text="Choose Class 1")
    c1Label.pack()
    chosenC1 = ttk.Combobox(Form1, values=Classes)
    chosenC1.pack()
    c2Label = Label(Form1, text="Choose Class 2")
    c2Label.pack()
    chosenC2 = ttk.Combobox(Form1, values=[])
    chosenC2.pack()

    def fillCB2Class(_):
        toRemove = chosenC1.get()
        chosenC2.set('')
        secList = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
        secList.remove(toRemove)
        chosenC2['values'] = secList

    b = Button(Form1, text="Start", command=lambda: Form1.quit())
    b.place(x=180, y=300)
    chosenC1.bind('<<ComboboxSelected>>', fillCB2Class)
    etaLabel = Label(Form1, text="Enter Learning rate(eta)")
    epochsLabel = Label(Form1, text="Enter number of epochs (m)")
    etaTB = Entry(Form1)
    epochsTB = Entry(Form1)
    var1 = IntVar()
    biasCheckbox = ttk.Checkbutton(Form1, variable=var1, text='add bias?', onvalue=1, offvalue=0)
    etaLabel.pack()
    etaTB.pack()
    epochsLabel.pack()
    epochsTB.pack()
    biasCheckbox.pack()
    Form1.mainloop()
    return chosenF1.get(), chosenF2.get(), chosenC1.get(), chosenC2.get(), etaTB.get(), epochsTB.get(),var1.get()
