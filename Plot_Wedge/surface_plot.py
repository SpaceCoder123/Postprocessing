import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

param1 = pd.read_csv('file1.csv')
param2 = pd.read_csv('file2.csv')
powerfactor = 1000000
param1['Modified_y'] = param1['Y_val']*powerfactor
length = 0.0508
param2['modified_X'] = param2['X_val']/length

plt.xlabel('X_val')
plt.ylabel('Y_val')

plt.plot(param1['X_val'], param1['Modified_y'],'*')
plt.plot(param2['modified_X'], param2['Y_val'])
plt.legend(['File1','File2'])
plt.show()