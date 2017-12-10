import  matplotlib.pylab as plt
import pandas as pd
import  numpy as np

import Component.Interpolar as inter


myf =  inter.Interpolar()
#inter.Interpolar.addPoint(1,1)


my_list = [ np.array([1,2,3]),np.array([3,4,3])]

data = {"y":[1,2,3],"y2":my_list}
df = pd.DataFrame(data)

plt.plot(df.iloc[:,0])

plt.show()
