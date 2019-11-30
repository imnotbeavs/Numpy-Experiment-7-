import numpy as np

X = np.zeros((10,10))
s = 0
for y in range(10):
    for z in range(10):
        s +=1
        X[y,z] = s**2

div3 = X[X%3==0]
np.save('div_by_3',div3)