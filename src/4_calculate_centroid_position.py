
"""
IN:     <prev_centroid>     <vector>
        <prev_centroid>     <vector>
        <prev_centroid>     <vector>
        ...

OUT:    <prev_centroid>     <new_centroid>
"""

import sys
import numpy as np


def get_centroid_and_vectors():
    """read the input from stdin"""

    vectors = []
    for l in sys.stdin:
        print('sdf')
        centroid, vector = l.split('\t')
        vector = [int(i) for i in vector.split(' ')]
        vectors.append(vector)

    return centroid, vectors


def calc_new_centroid(vectors):
    """calculate the new centroid from all the vectors"""
    return list(np.mean(vectors, axis=0))


def stringify_vector(vector):
    return ' '.join([str(i) for i in vector])


def main():
    original_centroid, vectors = get_centroid_and_vectors()

    new_centroid = calc_new_centroid(vectors)
    print("{}\t{}".format(
        original_centroid,
        stringify_vector(new_centroid)
    ))


main()
