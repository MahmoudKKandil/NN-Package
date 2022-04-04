import matplotlib.pyplot as plt


def DrawIris(Iris):
    fig, axs = plt.subplots(3, 2)
    class1=axs[0, 0].scatter(Iris.iloc[:50, 0], Iris.iloc[:50, 1],color = 'hotpink')
    class2=axs[0, 0].scatter(Iris.iloc[50:100, 0], Iris.iloc[50:100, 1],color = 'green')
    class3=axs[0, 0].scatter(Iris.iloc[100:150, 0], Iris.iloc[100:150, 1],color = 'blue')
    axs[0, 0].set_title("F1 vs F2")


    axs[1, 0].scatter(Iris.iloc[:50, 0], Iris.iloc[:50, 2],color = 'hotpink')
    axs[1, 0].scatter(Iris.iloc[50:100, 0], Iris.iloc[50:100, 2],color = 'green')
    axs[1, 0].scatter(Iris.iloc[100:150, 0], Iris.iloc[100:150, 2],color = 'blue')
    axs[1, 0].set_title("F1 vs F3")

    axs[2, 0].scatter(Iris.iloc[:50, 0], Iris.iloc[:50, 3],color = 'hotpink')
    axs[2, 0].scatter(Iris.iloc[50:100, 0], Iris.iloc[50:100, 3],color = 'green')
    axs[2, 0].scatter(Iris.iloc[100:150, 0], Iris.iloc[100:150, 3],color = 'blue')
    axs[2, 0].set_title("F1 Vs F4")

    axs[0, 1].scatter(Iris.iloc[:50, 1], Iris.iloc[:50, 2],color = 'hotpink')
    axs[0, 1].scatter(Iris.iloc[50:100, 1], Iris.iloc[50:100, 2],color = 'green')
    axs[0, 1].scatter(Iris.iloc[100:150, 1], Iris.iloc[100:150, 2],color = 'blue')
    axs[0, 1].set_title("F2 vs F3")

    axs[1, 1].scatter(Iris.iloc[:50, 1], Iris.iloc[:50, 3],color = 'hotpink')
    axs[1, 1].scatter(Iris.iloc[50:100, 1], Iris.iloc[50:100, 3],color = 'green')
    axs[1, 1].scatter(Iris.iloc[100:150, 1], Iris.iloc[100:150, 3],color = 'blue')
    axs[1, 1].set_title("F2 vs F4")

    axs[2, 1].scatter(Iris.iloc[:50, 2], Iris.iloc[:50, 3],color = 'hotpink')
    axs[2, 1].scatter(Iris.iloc[50:100, 2], Iris.iloc[50:100, 3],color = 'green')
    axs[2, 1].scatter(Iris.iloc[100:150, 2], Iris.iloc[100:150, 3],color = 'blue')
    axs[2, 1].set_title("F3 vs F4")
    plt.legend((class1, class2, class3),
                     ('Iris-setosa', 'Iris-versicolor', 'Iris-virginica'),
                     scatterpoints=1,
                     loc='center',
                     fontsize=6)
    fig.tight_layout()
    plt.show()
