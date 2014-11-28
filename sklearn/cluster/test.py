# coding: utf-8
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
ds = load_iris()
kmeans_model = KMeans()
kmeans_model.fit(ds.data)
