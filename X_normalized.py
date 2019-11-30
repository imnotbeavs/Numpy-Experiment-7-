import numpy as np

X = np.random.random((5,5))
mean = np.mean(X)
sdev = np.std(X)

Z = (X-mean)/sdev
print('X = ')
print(X)
print('Z = ')
print(Z)
np.save('X_normalized',Z)
