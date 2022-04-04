import seaborn as sns
import  matplotlib.pyplot as plt


def DrawMatrix(trueP,FalseP,FalseNeg,trueNeg):
    ax = sns.heatmap([[trueNeg,FalseP],[FalseNeg,trueP]], annot=True, cmap='Blues')

    ax.set_title('Seaborn Confusion Matrix with labels\n\n');
    ax.set_xlabel('\nPredicted Values')
    ax.set_ylabel('Actual Values ');

    ## Ticket labels - List must be in alphabetical order
    ax.xaxis.set_ticklabels(['False', 'True'])
    ax.yaxis.set_ticklabels(['False', 'True'])

    ## Display the visualization of the Confusion Matrix.
    plt.show()
    return