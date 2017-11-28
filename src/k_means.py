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
    return pd.DataFrame(doc_vals, index=doc_names)


def rest():
    vectorizer = TfidfVectorizer(stop_words='english')
    # maybe instead of this step - use the weights we have given, that way we use mostly our own code
    X = vectorizer.fit_transform(doc)

    # K-means here with a k of 3
    k_value = 3
    k_means = KMeans(n_clusters=k_value, init='k-means++',
                     max_iter=100, n_init=1)
    k_means.fit(X)

    clusters = k_means.labels_.tolist()
    print("the clusters are ", clusters)
    print("Top terms per cluster:")
    order_centroids = k_means.cluster_centers_.argsort()[:, ::-1]
    terms = vectorizer.get_feature_names()
    for i in range(k_value):
        print("Cluster %d:" % i,)
        for ind in order_centroids[i, :10]:
            print(' %s' % terms[ind],)
        print()


def main():
    df = get_input()
    print(df)


main()
