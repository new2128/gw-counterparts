'''
import importlib.util
package_name = 'scikit-misc'
spec = importlib.util.find_spec(package_name)
if spec is None:
     import os
     os.system(f"pip3 install scikit-misc")
'''
import sklearn
import matplotlib.pyplot as plt
import numpy as np
data = sklearn.datasets.make_circles(n_samples=80, factor=0.99)[0]
plt.scatter(data[:,0], data[:,1])