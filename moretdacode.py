#Currently the TDA code that works! 

from sklearn import datasets
import matplotlib.pyplot as plt
from ripser import ripser
from persim import plot_diagrams
import numpy as np

data = datasets.make_circles(n_samples=80, factor=0.99)[0]
#print(str(data))
print()
'''
plt.scatter(data[:,0], data[:,1])
extra_circle_data = np.concatenate([datasets.make_circles(n_samples=80, factor=0.99)[0],
              3+0.03*datasets.make_circles(n_samples=80, factor=0.99)[0]])
plt.scatter(extra_circle_data[:,0], extra_circle_data[:,1])
'''
diagrams = ripser(data)['dgms']
plot_diagrams(diagrams, show=True)
plt.show()