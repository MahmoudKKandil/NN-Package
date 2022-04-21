
import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
def Encode(iris,bias):

    X1=iris.iloc[:50, : ]
    X2 = iris.iloc[50:100,: ]
    X3= iris.iloc[100:150, :]

    X1 = X1.sample(frac=1).reset_index(drop=True)
    X1_Random , X1_test= train_test_split(X1,test_size=0.4,shuffle=True)
    X2 = X2.sample(frac=1).reset_index(drop=True)
    X2_Random,  X2_test = train_test_split(X2,test_size=0.4,shuffle=True)
    X3 = X3.sample(frac=1).reset_index(drop=True)
    X3_Random, X3_test = train_test_split(X3, test_size=0.4, shuffle=True)

    df3=pd.concat([X1_Random, X2_Random,X3_Random], ignore_index=True)
    df3.insert(0, "bias", bias)
    df3_rand = df3.sample(frac=1).reset_index(drop=True)
    df_Test = pd.concat([X1_test, X2_test,X3_test], ignore_index=True)
    df_Test.insert(0, "bias", bias)
    df_Test = df_Test.sample(frac=1).reset_index(drop=True)
    return df3_rand, df_Test





def Encode3(df,n):
    Y=np.zeros((n, 3))
    for index, row in df.iterrows():
        if row['Species']=="Iris-setosa":
            Y[index][0] = 1
            Y[index][1] = 0
            Y[index][2] = 0
        if row['Species']=="Iris-versicolor":
            Y[index][0] = 0
            Y[index][1] = 1
            Y[index][2] = 0
        if row['Species']=="Iris-virginica":
            Y[index][0] = 0
            Y[index][1] = 0
            Y[index][2] = 1
    return Y