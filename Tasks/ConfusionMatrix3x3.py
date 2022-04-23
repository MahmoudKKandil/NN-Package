
def CofusionMatrix(actual,predicted):
    cm = [[0] * 3 for _ in range(3)]
    for i in range(len(actual)):
        if actual[i]==predicted[i]:
            if(actual[i]=="SETOSA"):
                cm[0][0] +=1
            if (actual[i] == "VERSICOLR"):
                cm[1][1] +=1
            if (actual[i] == "VIRGINICA"):
                cm[2][2] += 1
        if actual[i] != predicted[i]:
            if actual[i] == "SETOSA" and predicted[i] == "VERSICOLR":
                cm[0][1]+=1
            elif actual[i] =="SETOSA" and predicted[i] == "VIRGINICA":
                cm[0][2] += 1
            elif actual[i] == "VERSICOLR" and predicted[i] == "SETOSA":
                cm[1][0] += 1
            elif actual[i] == "VERSICOLR" and predicted[i] == "VIRGINICA":
                cm[1][2] += 1
            elif actual[i] == "VIRGINICA" and predicted[i] == "SETOSA":
                cm[2][0] += 1
            elif actual[i] == "VIRGINICA" and predicted[i] == "VERSICOLR":
                cm[2][1] += 1

    return cm