from tkinter import *
from tkinter import ttk


def Task2MainForm():
    form2 = Tk()
    form2.geometry("400x450")
    form2.resizable(False, False)
    form2.title("Adaline training algorithm using MSE")
    featuresList = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']
    F1Label = Label(form2, text="Choose Feature 1")
    F1Label.pack()
    chosenF1 = ttk.Combobox(form2, values=featuresList)
    chosenF1.pack()
    F2Label = Label(form2, text="Choose Feature 2")
    F2Label.pack()
    chosenF2 = ttk.Combobox(form2, values=[])
    chosenF2.pack()

    def fillCB2(_):
        toRemove = chosenF1.get()
        chosenF2.set('')
        secList = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']
        secList.remove(toRemove)
        chosenF2['values'] = secList
    chosenF1.bind('<<ComboboxSelected>>', fillCB2)

    Classes = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
    c1Label = Label(form2, text="Choose Class 1")
    c1Label.pack()
    chosenC1 = ttk.Combobox(form2, values=Classes)
    chosenC1.pack()
    c2Label = Label(form2, text="Choose Class 2")
    c2Label.pack()
    chosenC2 = ttk.Combobox(form2, values=[])
    chosenC2.pack()

    def fillCB2Class(_):
        toRemove = chosenC1.get()
        chosenC2.set('')
        secList = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
        secList.remove(toRemove)
        chosenC2['values'] = secList

    b = Button(form2, text="Start", command=lambda: form2.quit())
    b.place(x=180, y=330)
    chosenC1.bind('<<ComboboxSelected>>', fillCB2Class)
    etaLabel = Label(form2, text="Enter Learning rate(eta)")
    epochsLabel = Label(form2, text="Enter number of epochs (m)")
    MSELabel = Label(form2, text="Enter MSE threshold ")
    etaTB = Entry(form2)
    epochsTB = Entry(form2)
    MSETB=Entry(form2)
    var1 = IntVar()
    biasCheckbox = ttk.Checkbutton(form2, variable=var1, text='add bias?', onvalue=1, offvalue=0)
    etaLabel.pack()
    etaTB.pack()
    epochsLabel.pack()
    epochsTB.pack()
    MSELabel.pack()
    MSETB.pack()
    biasCheckbox.pack()

    form2.mainloop()
    return chosenF1.get(), chosenF2.get(), chosenC1.get(), chosenC2.get(), etaTB.get(), epochsTB.get(),var1.get(),MSETB.get()
