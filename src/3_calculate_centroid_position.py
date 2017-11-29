
"""
IN:     <prev_centroid>     <vector>,<vector>,<vector>,...
OUT:    <prev_centroid>     <new_centroid>
"""

import sys
import numpy as np


def get_centroid_and_vectors():
    """read the input from command line"""
    centroid = sys.argv.split('\t')[0]

    lines = sys.argv.split('\t')[1]
    lines = [l.rstrip('\n') for l in lines]
    vectors = [
        float(v) for l in lines
        for v in l.split(' ')
    ]
    return centroid, np.array(vectors)


def calc_new_centroid(vectors):
    """calculate the new centroid from all the vectors"""
    return np.mean(vectors, axis=0)


def main():
    original_centroid, vectors = get_centroid_and_vectors()
    new_centroid = calc_new_centroid(vectors)
    print("{}\t{}".format(original_centroid, new_centroid))
