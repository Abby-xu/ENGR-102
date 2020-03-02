import matplotlib.pyplot as plt
import numpy as np

#graph 1
x=np.random.randint(0,100,100)
bins=np.arange(0,101,10)
width=10
print('data for the figure:',x)
frequency_each,_,_= plt.hist(x,bins,color='deepskyblue',width=width,alpha=0.7)
plt.xlabel('scores')
plt.ylabel('count')
plt.xlim(0,100)
plt.plot(bins[1:]-(width//2),frequency_each,color='palevioletred')
plt.show()

#graph 2
###box_plot
data = np.random.normal(size=1000, loc=0, scale=1)
print('data for the figure:',data)
plt.boxplot(data, sym="o", whis=1.5)
plt.show()