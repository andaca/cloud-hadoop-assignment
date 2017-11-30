#!/usr/bin/env python3

"""
IN:     <vector>    <centroid>,<centroid>,<centroid>,...
OUT:    <centroid>  <vector>
"""

import sys
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
import random


def get_vector_centroids():
    vector, centroids = list(sys.stdin)[0].split('\t')
    vector = [int(n) for n in vector.split(' ')]
    centroids = centroids.split(',')
    for i, c in enumerate(centroids):
        centroids[i] = [int(n) for n in c.split(' ')]
    return vector, centroids


def distance(vector, vector2):
    return np.sqrt(np.sum(np.square((vector - vector2))))


def nearest_centroid(vector, centroids):
    nearest, dist = None, float('inf')
    for i, c in enumerate(centroids):
        if distance(c, vector) < dist:
            nearest = centroids[i]
    return nearest


def stringify_vector(vector):
    return ' '.join([str(i) for i in vector])


def main():
    vector, centroids = get_vector_centroids()
    vector = np.array(vector)
    centroids = np.array(centroids)
    nearest_cent = nearest_centroid(vector, centroids)

    print("{}\t{}".format(
        stringify_vector(nearest_cent),
        stringify_vector(vector)
    ))


main()
