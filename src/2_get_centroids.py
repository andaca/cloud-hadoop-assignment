#!/usr/bin/env python3

"""
IN:     "KEY"     <vector>

OUT:    <vector>    <centroid>,<centroid>,<centroid>,...
        <vector>    <centroid>,<centroid>,<centroid>,...
        <vector>    <centroid>,<centroid>,<centroid>,...
        ...
"""
import random
import sys


def get_vectors():
    vector_strings = [l.split('\t')[1] for l in sys.stdin]
    vector_strings = [vs.rstrip('\n') for vs in vector_strings]
    vectors = [vs.split(' ') for vs in vector_strings]

    for i, v in enumerate(vectors):
        v = [i for i in v if i]
        vectors[i] = [int(i) for i in v]
    return vectors


def stringify_vector(vector):
    return ' '.join([str(i) for i in vector])


def read_centroids_from_reducer_out_file(fname):
    with open(fname, 'rt') as f:
        centroids = [l.split('\t')[1] for l in f.readlines()]
        centroids = [c.rstrip('\n') for c in centroids]
        centroids = [c.split(' ') for c in centroids]

        for i, centroid in enumerate(centroids):
            centroid = [i for i in centroid if i]
            centroids[i] = [int(i) for i in centroid]

        return centroids


def random_centroids(vectors, N_CENTROIDS=5):
    # pick random centroids
    # Use a set to ensure they are all unique.
    # Sets have to be of tuples rather than lists, since lists are mutable
    centroids = set()
    while len(centroids) != N_CENTROIDS:
        centroids.add(tuple(vectors[random.randint(0, len(vectors) - 1)]))

    # Now you can cast the set of tuples to a list of lists
    return [list(c) for c in centroids]


def main():
    N_CENTROIDS = 5
    REDUCER_OUT_FNAME = "part-0000"
    vectors = get_vectors()
    try:
        centroids = read_centroids_from_reducer_out_file(REDUCER_OUT_FNAME)
    except FileNotFoundError:   # thrown on the first run
        centroids = random_centroids(vectors, N_CENTROIDS)

    for v in vectors:
        print("{}\t{}".format(
            stringify_vector(v),
            ','.join([stringify_vector(c) for c in centroids])
        ))


main()
