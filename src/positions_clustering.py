import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import seaborn as sns
from kneed import KneeLocator
from pathlib import Path

cwd = Path.cwd()
root = cwd.parent.absolute()

stats = pd.read_csv(root / 'data' / 'combined_stats.csv')
stats = stats.dropna()

stats['TS Add Per 36'] = stats['TS Add']/stats['G']*36/stats['mins']
stats['AST Per 36'] = (stats['AST']+stats['FT_AST'])*36/stats['mins']

X = stats[['2P', '3P', 'FTr', '3PAr', 'TS Add Per 36', 'AST Per 36', 'PLUSMINUS', 'o_reb_pct', 'stl_pct', 'tov_pct', 'd_reb_pct', 'usg_pct']]
X = (X-X.mean())/X.std()

sse = []
for k in range(1, 21):
	kmeans = KMeans(n_clusters = k, random_state = 0, n_init='auto')
	kmeans.fit(X)
	sse.append(kmeans.inertia_)

plt.style.use("fivethirtyeight")
plt.plot(range(1, 21), sse)
plt.xticks(range(1, 21))
plt.xlabel("Number of Clusters")
plt.ylabel("SSE")
plt.show()


kl = KneeLocator(range(1, 21), sse, curve="convex", direction="decreasing")
print("Elbow is: ", kl.elbow)


kmeans = KMeans(n_clusters = 8, random_state = 0, n_init='auto')
kmeans.fit(X)


cols = X.columns
player_clusters = []
for i in range(8):
	player_clusters.append([])

for i, v in enumerate(kmeans.labels_):
	player_clusters[v].append(stats.iloc[i, 1])

for i, v in enumerate(player_clusters):
	print('cluster', i+1)
	for j in range(len(kmeans.cluster_centers_[i])):
		print(cols[j], ':', kmeans.cluster_centers_[i][j])
	print('players:', v)
	print('\n')



"""
Cluster 1: 
inefficient players- low 2 point percentage, low 3 point percentage

Cluster 2:
big men- high 2 point percentage, low 3 point attempt rate, high offensive and defensive rebound percentages

Cluster 3:
high usage players- high usage rate, above average assists per 36, above average efficiency, above average free throw rate

Cluster 4:
all around players- slightly above average in many categories

Cluster 5:
ball handlers- high assists per 36, but not very efficient

Cluster 6:
perimeter defenders- high steal percentage

Cluster 7:
3 point shooters- high 3 point attempt rate

Cluster 8:
big men who hit one or two 3's so their percentage is unusually high and their 3 point attempt rate is low 
"""



