# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 12:13:14 2022

@author: ladae
"""

# importing the libraries
import numpy as np
import  matplotlib.pyplot as plt
import pandas as pd

# importing dataset with pandas
dataset = pd.read_csv("Mall_Customers.csv")
x = dataset.iloc[:, [3,4]].values

# Using dendogram to find the optimal number of clusters
import scipy.cluster.hierarchy as sch
dendogram = sch.dendrogram(sch.linkage(x, method="ward"))
plt.title("Dendogram")
plt.xlabel("Customers")
plt.ylabel("Euclidean Distances")
plt.show()

# Fitting hierchical clustering to the dataset
from sklearn.cluster import AgglomerativeClustering
hc = AgglomerativeClustering(n_clusters=5, affinity = "euclidean", linkage="ward")
y_hc = hc.fit_predict(x)

# Visualizing the clusters
plt.scatter(x[y_hc == 0,0], x[y_hc == 0, 1], s = 100, c = 'red', label = "Careful")
plt.scatter(x[y_hc == 1,0], x[y_hc == 1, 1], s = 100, c = 'blue', label = "Standard")
plt.scatter(x[y_hc == 2,0], x[y_hc == 2, 1], s = 100, c = 'green', label = "Target")
plt.scatter(x[y_hc == 3,0], x[y_hc == 3, 1], s = 100, c = 'cyan', label = "Carelesss")
plt.scatter(x[y_hc == 4,0], x[y_hc == 4, 1], s = 100, c = 'magenta', label = "Sensible")
plt.title("Clusters of clients")
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (1-100)")
plt.legend()
plt.show()