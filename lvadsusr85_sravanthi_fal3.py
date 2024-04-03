# -*- coding: utf-8 -*-
"""LVADSUSR85_Sravanthi_fal3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rTI8eC_eg0wo6uCOP56X85_ls77efBJ0
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder,StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,classification_report
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA

data = pd.read_csv('/content/seeds.csv')
df = pd.DataFrame(data)
print(df.isnull().sum(),end='\n\n')
print(df.info())
print(df)

df.fillna(df['Area'].mean(),inplace=True)
df.fillna(df['Perimeter'].mean(),inplace=True)
df.fillna(df['Compactness'].mean(),inplace=True)
df.fillna(df['Length of kernel'].mean(),inplace=True)
df.fillna(df['Width of kernel'].mean(),inplace=True)
df.fillna(df['Asymmetry coefficient'].mean(),inplace=True)
df.fillna(df['Length of kernel groove'].mean(),inplace=True)
df.isnull().sum()

sns.heatmap(df.corr())
plt.show()

scaler = StandardScaler()
X_scaled = scaler.fit_transform(df)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

silhouette_scores = []
for k in range(2, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    silhouette_scores.append(silhouette_score(X_scaled, kmeans.labels_))
print(silhouette_scores)

plt.plot(range(2,11), silhouette_scores, marker='o')
plt.xlabel('Number of Clusters')
plt.ylabel('Silhouette Score')
plt.title('Silhouette Score vs Number of Clusters')
plt.show()

sse = []
for i in range(2,11):
  model = KMeans(n_clusters = i)
  model.fit(X_scaled)
  sse.append(model.inertia_)

plt.plot(range(2,11),sse,marker = 'o')
plt.title("elbow method")
plt.xlabel('clusters')
plt.ylabel('sse')
plt.show()

k = 3

kmeans = KMeans(n_clusters=k, random_state=42)
kmeans.fit(df)

clusters = kmeans.predict(df)


plt.scatter(X_pca[:,0], X_pca[:,1], c=clusters, cmap='viridis')
plt.xlabel('PCA Component-1')
plt.ylabel('PCA Component-2')
plt.title('K-means Clustering')
plt.show()