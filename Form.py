from tkinter import *
from tkinter import ttk

def Task1MainForm():
    mForm1=Tk()
    mForm1.geometry("700x700")
    featuresList = ['F1 sepal length (cm)', 'F2 sepal width (cm)', 'F3 petal length (cm)', 'F4 petal width (cm)']
    F1Label = Label(mForm1, text="Choose F1")
    F1Label.pack()
    chosenF1 = ttk.Combobox(mForm1,values=featuresList)
    chosenF1.pack()
    F2Label = Label(mForm1, text="Choose F2")
    F2Label.pack()
    chosenF2 = ttk.Combobox(mForm1,values=[])
    chosenF2.pack()
    def fillCB2(_):
        toRemove = chosenF1.get()
        chosenF2.set('')
        secList = ['F1 sepal length (cm)', 'F2 sepal width (cm)', 'F3 petal length (cm)', 'F4 petal width (cm)']
        secList.remove(toRemove)
        chosenF2['values'] = secList
    chosenF1.bind('<<ComboboxSelected>>', fillCB2)

    Classes = ['C1','C2','C3']
    c1Label = Label(mForm1, text="Choose Class 1")
    c1Label.pack()
    chosenC1 = ttk.Combobox(mForm1, values=Classes)
    chosenC1.pack()
    c2Label = Label(mForm1, text="Choose Class 2")
    c2Label.pack()
    chosenC2 = ttk.Combobox(mForm1, values=[])
    chosenC2.pack()

    def fillCB2Class(_):
        toRemove = chosenC1.get()
        chosenC2.set('')
        secList = ['C1','C2','C3']
        secList.remove(toRemove)
        chosenC2['values'] = secList

    chosenC1.bind('<<ComboboxSelected>>', fillCB2Class)
    etaLabel = Label(mForm1, text="Enter Learning rate(eta)")
    epochsLabel = Label(mForm1, text="Enter number of epochs (m)")
    etaTB = Entry(mForm1)
    epochsTB = Entry(mForm1)
    var1 = IntVar()
    biasCheckbox = ttk.Checkbutton(mForm1, variable=var1, text='add bias?', onvalue=1, offvalue=0)
    etaLabel.pack()
    etaTB.pack()
    epochsLabel.pack()
    epochsTB.pack()
    biasCheckbox.pack()


    mForm1.mainloop()