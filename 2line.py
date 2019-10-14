from matplotlib import pyplot as plt
import warnings
warnings.filterwarnings('ignore')
X1=[1,2,3]
Y1=[2,4,1]
plt.plot(X1,Y1,linewidth=2.0,label="line1")
X2=[1,2,3]
Y2=[4,1,3]
plt.plot(X2,Y2,linewidth=2.0,label="line2")
plt.xlabel('x -label')
plt.ylabel('y -label')
plt.title("my graph 2")
plt.legend()
plt.show()
