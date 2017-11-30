#!/usr/bin/env python3

"""
Prints either `TRUE` or `FALSE`

Expects the name of a file containing two comma-delimited vectors per line.
For each line, checks to see if the distance between the two vectors is greater
than the ACCEPTABLE_MARGIN constant.
"""

import sys
import numpy as np


def get_fname():
    return sys.argv[1]


def get_centroid_pairs(fname):
    """read the input from stdin"""
    centroids = []
    with open(fname) as f:
        for l in f.readlines():
            c1, c2 = l.split('\t')
            c1 = [int(i) for i in c1.split(' ')]
            c2 = [int(i) for i in c2.split(' ')]
            centroids.append((c1, c2))
    return centroids


def distance(vector, vector2):
    return np.sqrt(np.sum(np.square((vector - vector2))))


def main():
    ACCEPTABLE_MARGIN = 100  # This needs to be tweaked depending on the data
    centroid_pairs = get_centroid_pairs(get_fname())
    for c1, c2 in centroid_pairs:
        if distance(np.array(c1), np.array(c2)) > ACCEPTABLE_MARGIN:
            raise SystemExit("TRUE")
    print("FALSE")


main()
