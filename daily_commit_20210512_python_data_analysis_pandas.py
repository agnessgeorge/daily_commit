import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('tips.csv')
print (df.head())
print(" ")
x = [1,2,3,4,5,6,7,8]
y =[1,4,9,16,25,36,49,64]
plt.plot(x, y, 'r') # 'r' is the color red
plt.xlabel('X Axis Title Here')
plt.ylabel('Y Axis Title Here')
plt.title('String Title Here')
plt.show()