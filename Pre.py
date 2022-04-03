from sklearn import preprocessing


def Encode(iris, class1, class2):
    if class1 == 1 and class2 == 2:
        NewIris = iris[0:50]
        NewIris = NewIris.sample(frac=1)
        NewIris2 = iris[50:100]
        NewIris2 = NewIris2.sample(frac=1)
        NewIris = NewIris.append(NewIris2)
        label_encoder = preprocessing.LabelEncoder()
        NewIris['Species'] = label_encoder.fit_transform(NewIris['Species'])
        return NewIris
    elif class1 == 1 and class2 == 3:
        NewIris = iris[0:50]
        NewIris = NewIris.sample(frac=1)
        NewIris2 = iris[100:150]
        NewIris2 = NewIris2.sample(frac=1)
        NewIris = NewIris.append(NewIris2)
        label_encoder = preprocessing.LabelEncoder()
        NewIris['Species'] = label_encoder.fit_transform(NewIris['Species'])
        return NewIris
    else:
        NewIris = iris[50:100]
        NewIris = NewIris.sample(frac=1)
        NewIris2 = iris[100:150]
        NewIris2 = NewIris2.sample(frac=1)
        NewIris = NewIris.append(NewIris2)
        label_encoder = preprocessing.LabelEncoder()
        NewIris['Species'] = label_encoder.fit_transform(NewIris['Species'])
        return NewIris


def Prepro(iris, feature1, feature2):
    if feature1 == 'F1 sepal length (cm)' and feature2 == 'F2 sepal width (cm)':
        iris = iris[['SepalLengthCm', 'SepalWidthCm', 'Species']]

    elif feature1 == 'F2 sepal width (cm)' and feature2 == 'F1 sepal length (cm)':
        iris = iris[['SepalLengthCm', 'SepalWidthCm', 'Species']]

    elif feature1 == 'F1 sepal length (cm)' and feature2 == 'F3 petal length (cm)':
        iris = iris[['SepalLengthCm', 'PetalLengthCm', 'Species']]

    elif feature1 == 'F3 petal length (cm)' and feature2 == 'F1 sepal length (cm)':
        iris = iris[['SepalLengthCm', 'PetalLengthCm', 'Species']]

    elif feature1 == 'F1 sepal length (cm)' and feature2 == 'F4 petal width (cm)':
        iris = iris[['SepalLengthCm', 'PetalWidthCm', 'Species']]

    elif feature1 == 'F4 petal width (cm)' and feature2 == 'F1 sepal length (cm)':
        iris = iris[['SepalLengthCm', 'PetalWidthCm', 'Species']]

    elif feature1 == 'F2 sepal width (cm)' and feature2 == 'F3 petal length (cm)':
        iris = iris[['SepalWidthCm', 'PetalLengthCm', 'Species']]

    elif feature1 == 'F3 petal length (cm)' and feature2 == 'F2 sepal width (cm)':
        iris = iris[['SepalWidthCm', 'PetalLengthCm', 'Species']]

    elif feature1 == 'F2 sepal width (cm)' and feature2 == 'F4 petal width (cm)':
        iris = iris[['SepalWidthCm', 'PetalWidthCm', 'Species']]

    elif feature1 == 'F4 petal width (cm)' and feature2 == 'F2 sepal width (cm)':
        iris = iris[['SepalWidthCm', 'PetalWidthCm', 'Species']]

    else:
        iris = iris[['PetalLengthCm', 'PetalWidthCm', 'Species']]
    return iris
