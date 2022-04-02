import matplotlib.pyplot as plt


def DrawIris(Iris):
    fig, axs = plt.subplots(3, 2)
    axs[0, 0].scatter(Iris.data[:51, 0], Iris.data[:51, 1])
    axs[0, 0].scatter(Iris.data[51:101, 0], Iris.data[51:101, 1])
    axs[0, 0].scatter(Iris.data[101:151, 0], Iris.data[101:151, 1])
    axs[0, 0].set_title("F1 vs F2")

    axs[1, 0].scatter(Iris.data[:51, 0], Iris.data[:51, 2])
    axs[1, 0].scatter(Iris.data[51:101, 0], Iris.data[51:101, 2])
    axs[1, 0].scatter(Iris.data[101:151, 0], Iris.data[101:151, 2])
    axs[1, 0].set_title("F1 vs F3")

    axs[2, 0].scatter(Iris.data[:51, 0], Iris.data[:51, 3])
    axs[2, 0].scatter(Iris.data[51:101, 0], Iris.data[51:101, 3])
    axs[2, 0].scatter(Iris.data[101:151, 0], Iris.data[101:151, 3])
    axs[2, 0].set_title("F1 Vs F4")

    axs[0, 1].scatter(Iris.data[:51, 1], Iris.data[:51, 2])
    axs[0, 1].scatter(Iris.data[51:101, 1], Iris.data[51:101, 2])
    axs[0, 1].scatter(Iris.data[101:151, 1], Iris.data[101:151, 2])
    axs[0, 1].set_title("F2 vs F3")

    axs[1, 1].scatter(Iris.data[:51, 1], Iris.data[:51, 3])
    axs[1, 1].scatter(Iris.data[51:101, 1], Iris.data[51:101, 3])
    axs[1, 1].scatter(Iris.data[101:151, 1], Iris.data[101:151, 3])
    axs[1, 1].set_title("F2 vs F4")

    axs[2, 1].scatter(Iris.data[:51, 2], Iris.data[:51, 3])
    axs[2, 1].scatter(Iris.data[51:101, 2], Iris.data[51:101, 3])
    axs[2, 1].scatter(Iris.data[101:151, 2], Iris.data[101:151, 3])
    axs[2, 1].set_title("F3 vs F4")

    fig.tight_layout()
    plt.show()