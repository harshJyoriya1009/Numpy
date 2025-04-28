import numpy as np
x=np.array([[1,2],[3,4]])
y=np.array([[7,8],[6,7]])

z=np.concatenate((x,y),axis=0)
print(z)
