import pandas as pd
import Plotter
import form2

iris = pd.read_csv("Iris.csv")
df = pd.DataFrame(iris)
Plotter.DrawIris(iris)

form2.Task2MainForm(iris)

