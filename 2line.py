from matplotlib import pyplot as plt
import warnings
warnings.filterwarnings('ignore')
X1=[3,2,1]
Y1=[1,4,2]
plt.plot(X1,Y1,linewidth=3.0,label="1stline")
X2=[2,1,3]
Y2=[1,3,4]
plt.plot(X2,Y2,linewidth=3.0,label="2ndline")
plt.xlabel('x -label')
plt.ylabel('y -label')
plt.title("my 2nd graph")
plt.legend()
plt.show()
