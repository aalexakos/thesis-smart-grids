import pandas as pd 
import json as jsn
import matplotlib.pyplot as plt 
import numpy as np

df=pd.read_csv('data', sep = ';')

data={}
for col in df.columns:
    data.clear
    for row in df[col]:
        if(row in data.keys()):
            data[row]= data[row] + 1
        else:
            data[row]=1

    print (jsn.dumps(data,sort_keys=True, indent=4))

    # Data to plot
    labels = []
    sizes = []

    for x, y in data.items():
        labels.append(x)
        sizes.append(y)

    # Plot
    plt.pie(sizes, labels=labels)

    plt.axis('equal')
    plt.show()
    