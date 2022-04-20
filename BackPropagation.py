import numpy as np
import random
import math


def ActivationFunction(net,Function):
  if Function=="SigmoidFunction":
      result= 1/(1 + np.exp(-1*net))
  else:
      result = math.tanh(net)
  return result
def BackActivationFunction(net,Function):
  if Function=="SigmoidFunction":
      result= net*(1-net)

  else:
      result = (1-net)*(1+net)
  return result
def forward(NumberOfLayers,row,weights,bias,ActivFunction):
    arrayOfnet=[]
    for i in range(NumberOfLayers + 1):
     weight = np.array(weights[i])
     net = weight.dot(row)
     result=ActivationFunction(net,ActivFunction)
     arrayOfnet.append(result)
     #7zawed el bias lel next iteration
     row=np.insert(result, 0, bias, axis=0)
    return arrayOfnet


def back(arrayOfnetarrays,ActivFunction,weights,TrainY,NumberOfLayers):
    count=NumberOfLayers
    arrOfSArrays=[]
    newS=[]
    while(count>-1):
        nomOfNurons=len(arrayOfnetarrays[count])
        if(arrOfSArrays!=[]):
            lastArrIndex=len(arrOfSArrays)-1
            oldS=arrOfSArrays[lastArrIndex]
        for i in range(nomOfNurons):
                if(count==NumberOfLayers):
                        sNet=(TrainY[i]-arrayOfnetarrays[count][i])*BackActivationFunction(arrayOfnetarrays[count][i],ActivFunction)

                else:
                    for j in range(len(oldS)):
                        sNet+=(oldS[j]*weights[count+1][j][i+1])
                    sNet*=BackActivationFunction(arrayOfnetarrays[count][i],ActivFunction)
                newS.append(sNet)
                sNet=0
        count-=1
        arrOfSArrays.append(newS);
        newS=[]
    return arrOfSArrays
def updatewights(arrOfSArrays,arrayOfnetarrays,weights,l_rate,bias,NumberOfLayers,row):
    for i in range(len(weights)):#layers
        for j in range(len(weights[i])):#neron index
            for k in range(len(weights[i][j])):#weight index eli daa5el flneron index
                if i==0 :
                    x=row[k]
                elif(bias==1 and k==0):
                       x=1
                elif (bias == 0 and k == 0):
                       x = 0
                else:
                        # i-1 3shan elnet bybtdi mn awl layer b3d elinput, fah index ellayer hyb2a 1 eli hwa i bs elindex flnet 0
                     x = arrayOfnetarrays[i - 1][k - 1]

                s = arrOfSArrays[i][j]
                weights[i][j][k]= weights[i][j][k]+(l_rate*s*x)
    return weights




def create_array(m, n):
    arr = []
    for i in range(m):
        col = []
        for j in range(n):
            col.append(random.uniform(-1, 1))

        arr.append(col)

    return arr


def initialize_weights(NumberOfLayers,neurons,numberOfFeatures):
    ind = 0
    m = neurons[ind]
    n = numberOfFeatures+1
    weights = []
    for i in range(NumberOfLayers + 1):
        arr = create_array(m, n)
        weights.append(arr)
        if(i==NumberOfLayers):
            break
        ind = ind + 1;
        m = neurons[ind];
        n = neurons[ind-1]+1;

    return weights


def Train(trainX, TrainY, l_rate, n_epoch,NumberOfLayers,neurons,numberOfFeatures,bias,ActivFunction):
    trainX = np.array(trainX)
    weights = initialize_weights(NumberOfLayers,neurons,numberOfFeatures)

    #bab3at el number of features 3shan de 3adad el neurons bta3et el input layer
    for epoch in range(n_epoch):
        for i, row in enumerate(trainX):
            arrayOfnetarrays = forward(NumberOfLayers,row, weights,bias,ActivFunction)
            arrOfSArrays=back(arrayOfnetarrays,ActivFunction,weights,TrainY[i],NumberOfLayers)
            arrOfSArrays=arrOfSArrays[::-1]
            #arrOfSArrays=np.flipud(arrOfSArrays)#ana 3mlt reverse llarray 3shan 25li ellocal gradient bta3 eloutput hwa eli fl25er w yb2a bnfs tarteb elarray eli feh elnet
            res= updatewights(arrOfSArrays,arrayOfnetarrays,weights,l_rate,bias,NumberOfLayers,row)

    return res
def test_Data(testX, testY, weights,NumberOfLayers,bias,ActivFunction):
    testX = np.array(testX)
    correct=0
    predArr=[]
    for i, row in enumerate (testX):
        arrayOfnetarrays = forward(NumberOfLayers, row, weights, bias, ActivFunction)
        result = np.where(arrayOfnetarrays[NumberOfLayers] == np.amax(arrayOfnetarrays[NumberOfLayers]))
        arrayOfnetarrays[NumberOfLayers][result]=1
        newArr=Zerohat(arrayOfnetarrays[NumberOfLayers])
        if  np.array_equal(newArr, testY[i]):
            correct += 1
        predArr.append(newArr)
    accuracy = (correct / len(testX)) * 100
    testY=np.array(testY)
    predArr = np.array(predArr)
    testY=CreateConf( testY)
    predArr = CreateConf(predArr)
    return accuracy,testY,predArr
def Zerohat(arr):
    for i in range(len(arr)):
        if (arr[i] != 1):
            arr[i]=0
    return arr
def CreateConf(arr):
 newArr=[]
 for i in range(len(arr)):
     if np.array_equal(arr[i], [1,0,0]):
         newArr.append("SETOSA")
     elif np.array_equal(arr[i], [0,1,0]):
         newArr.append("VERSICOLR")
     elif np.array_equal(arr[i], [0,0,1]):
         newArr.append("VIRGINICA")
 newArr=np.array(newArr)
 return newArr