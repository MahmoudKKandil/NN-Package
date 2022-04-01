import matplotlib.pyplot as plt

x=[1,2,3,4]
y=[1,2,5,10]

x2=[1,2,3,4]
y2=[5,8,12,20]

plt.figure("fig1")
plt.scatter(x,y)
plt.scatter(x2,y2)

plt.show()