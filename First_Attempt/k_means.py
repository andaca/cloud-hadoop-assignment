from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score
import sys
import pandas as pd


# https://stackoverflow.com/questions/27889873/clustering-text-documents-using-scikit-learn-kmeans-in-python
def get_input():
    lines = [l.rstrip('\n') for l in sys.stdin]
    lines = [l.split('\t')[1] for l in lines]
    doc_names = [l.split(' ')[0] for l in lines]
    doc_vals = [l.split(' ')[1:] for l in lines]
  
    # do this to make the 2D array a single array - for the k_means to work
    doc_vals_flat = [item for sublist in doc_vals for item in sublist]
  

    #return pd.DataFrame(doc_vals, index=doc_names), doc_vals
    return pd.DataFrame(doc_vals, index=doc_names), doc_vals_flat


def k_means_clustering(df, values):
    # K-means here with a k of 5
    k_value = 5
    k_means = KMeans(n_clusters=k_value, init='k-means++',
                     max_iter=100, n_init=1)
    #k_means.fit(X)
    k_means.fit(df)

    clusters = k_means.labels_.tolist()
    print("the clusters are ", clusters)
    print("Top terms per cluster:")
    order_centroids = k_means.cluster_centers_.argsort()[:, ::-1]
    terms = values
    for i in range(k_value):
        print("Cluster %d:" % i,)
        for ind in order_centroids[i, :10]:
            print(' %s' % terms[ind],)
        print()


def main():
    df, vals = get_input()
    k_means_clustering(df,vals)


main()