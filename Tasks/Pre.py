from sklearn import preprocessing
import pandas as pd
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split

def Encode(iris, class1, class2,f1,f2,bias):
    index_noF1 = iris.columns.get_loc(f1)
    index_noF2 = iris.columns.get_loc(f2)
    if (class1 == "Iris-setosa" and class2 == "Iris-versicolor" ):
        X1=iris.iloc[:50, [index_noF1,index_noF2,5] ]
        X2 = iris.iloc[50:100, [index_noF1,index_noF2,5] ]
    elif (class1 =="Iris-setosa" and class2 == "Iris-virginica") :
        X1 = iris.iloc[:50, [index_noF1,index_noF2,5] ]
        X2 = iris.iloc[100:150, [index_noF1,index_noF2,5] ]
    elif class1 == "Iris-virginica" and class2 == "Iris-setosa":
        X1 = iris.iloc[100:150, [index_noF1, index_noF2,5]]
        X2 = iris.iloc[:50, [index_noF1, index_noF2,5]]
    elif (class1 == "Iris-versicolor" and class2 == "Iris-setosa"):
        X1 = iris.iloc[50:100, [index_noF1, index_noF2,5]]
        X2 = iris.iloc[:50, [index_noF1, index_noF2,5]]
    elif (class1 == "Iris-versicolor" and class2 == "Iris-virginica" ):
        X1 = iris.iloc[50:100, [index_noF1,index_noF2,5] ]
        X2 = iris.iloc[100:150, [index_noF1,index_noF2,5] ]
    elif (class1 == "Iris-virginica" and class2 == "Iris-versicolor"):
        X1 = iris.iloc[100:150, [index_noF1, index_noF2,5]]
        X2 = iris.iloc[50:100, [index_noF1, index_noF2,5]]

    X1 = X1.sample(frac=1).reset_index(drop=True)
    X1_Random , X1_test1= train_test_split(X1,test_size=0.4,shuffle=True)
    X2 = X2.sample(frac=1).reset_index(drop=True)
    X2_Random,  X2_test2 = train_test_split(X2,test_size=0.4,shuffle=True)

    df3=pd.concat([X1_Random, X2_Random], ignore_index=True)
    df3.insert(0, "bias", bias)
    df3_rand = df3.sample(frac=1).reset_index(drop=True)

    df_Test = pd.concat([X1_test1, X2_test2], ignore_index=True)
    df_Test.insert(0, "bias", bias)
    df_Test = df_Test.sample(frac=1).reset_index(drop=True)

    return df3_rand, df_Test,df3





def Encode2(df, class1):
    Y=[]
    for index, row in df.iterrows():
        if row['Species']==class1:
            Y.append(1)
        else:
            Y.append(-1)
    return Y