from matplotlib import pyplot as plt
import warnings
warnings.filterwarnings('ignore')
X'=[3,2,1]
Y'=[1,4,2]
plt.plot(X',Y',linewidth=3.0,label="1stline")
X''=[2,1,3]
Y''=[1,3,4]
plt.plot(X'',Y'',linewidth=3.0,label="2ndline")
plt.xlabel('x -label')
plt.ylabel('y -label')
plt.title("my 2nd graph")
plt.legend()
plt.show()
