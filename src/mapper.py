#!/usr/bin/env python3

import sys
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
import random


def file_names():
    return sys.argv[1:]


def get_words(fname):
    with open(fname, 'rt') as f:
        return ' '.join([l for l in f.readlines()])


def remove_unwanted_words(words):
    # Do it here
    return ' '.join([word for word in words.split(' ') if True])


def vectorise(words_lists, file_names):
    # https://stackoverflow.com/questions/15899861/efficient-term-document-matrix-with-nltk
    vec = CountVectorizer()
    X = vec.fit_transform(words_lists)
    df = pd.DataFrame(X.toarray(),
                      columns=vec.get_feature_names(),
                      index=[i for i in file_names])  # set up the table
    return df


def distance(vector, vector2):
    return np.sqrt(np.sum(np.square((vector - vector2))))


def nearest_centroid(centroids, vector):
    nearest, dist = None, float('inf')
    for i, c in enumerate(centroids):
        if distance(c, vector) < dist:
            nearest = centroids[i]
    return nearest


def main():
    N_CENTROIDS = 5
    # get the file names
    fnames = file_names()

    # read the words from the files into a list of strings
    file_words = []
    for fname in fnames:
        try:
            words = get_words(fname)
            file_words.append(words)
        except:
            fnames.remove(fname)

    # vectorise the files words
    vectors = vectorise(file_words, fnames)

    # pick random centroids
    random_centroids = set()
    while len(random_centroids) != N_CENTROIDS:
        random_centroids.add(vectors[random.randint(0, len(vectors))])

    # print the nearest centroid as a key, the vector as the value
    for v in vectors:
        print("{}\t{}".format(nearest_centroid(random_centroids, v), v))


main()
