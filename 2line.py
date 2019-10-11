from matplotlib import pyplot as plt
x1=[1,2,3]
y1=[2,4,1]
plt.plot(x1,y1,linewidth=2.0,label="line1")
x2=[1,2,3]
y2=[4,1,3]
plt.plot(x2,y2,linewidth=2.0,label="line2")
plt.xlabel('x -label')
plt.ylabel('y -label')
plt.title("my graph 2")
plt.legend()
plt.show()
