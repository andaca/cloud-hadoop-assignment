#!/usr/bin/env python3
"""

IN:     fname       <vector>
        fname       <vector>
        fname       <vector>
        ...

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


def main():
    N_CENTROIDS = 5

    vectors = get_vectors()

    # pick random centroids
    # Use a set to ensure they are all unique.
    # Sets have to be of tuples rather than lists, since lists are mutable
    centroids = set()
    while len(centroids) != N_CENTROIDS:
        centroids.add(tuple(vectors[random.randint(0, len(vectors) - 1)]))

    # Now you can cast the set of tuples to a list of lists
    centroids = [list(c) for c in centroids]

    for v in vectors:
        print("{}\t{}".format(
            stringify_vector(v),
            ','.join([stringify_vector(c) for c in centroids])
        ))


main()
