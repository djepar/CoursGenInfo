import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model 


def corrcoef(x, y):
    x = (25, 26, 22, 30, 27, 23, 22)
    y = (7, 14, 16, 22, 29, 16, 26)
    return np.corrcoef(x, y)



x = np.array([25, 26, 22, 30, 27, 23, 22])
y = np.array([7, 14, 16, 22, 29, 16, 26])
k, d = np.polyfit(x, y, 1)
y_pred = k*x + d

plt.plot(x, y, '.')
plt.plot(x, y_pred)
plt.show()

x = np.array([25, 26, 22, 30, 27, 23, 22]).reshape((-1,1))
print(x.shape)
reg.fit(x,y)