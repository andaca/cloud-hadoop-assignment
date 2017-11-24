import math
import sys
import numpy
from sklearn.decomposition import PCA


def get_input():
    # returns a tuple of the filenames, and a numpy array of arrays of counts
    # order is preserved, so they can be zipped back together again later
    data = [
        ('file1', [1, 0, 2, 3, 4]),
        ('file2', [6, 3, 5, 7, 9]),
        ('file3', [7, 12, 0, 2, 4]),
        ('file4', [3, 5, 7, 2, 4]),
    ]
    fnames, counts = zip(*data)
    return fnames, numpy.array(counts)


def reduce_dimensions(data):
    """
    @args: data - a numpy array containing arrays of numbers e.g.: [[1,2,3], [4,5,6], ...]
    @returns: a new numpy array containing arrays of numbers
    """
    # Use Principle Component Analysis to reduce the dimensions
    # http://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html
    # TODO: Can specify n_components in when initialising PCA. Not sure if/what should be used.
    return PCA().fit_transform(data)


def chunk(iterable, n):
    """Takes something which you can iterate over, and breaks it into n lists.
    The final list is not padded, so may be shorter than chunk_size.
    https://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks
    """
    chunk_size = math.ceil(len(iterable) / n)
    for i in range(0, len(iterable), chunk_size):
        yield iterable[i: i + chunk_size]


def main():
    N_CHUNKS = 2  # the number of chunks the data will be split into for parallel reducing

    fnames, word_counts = get_input()
    word_counts = reduce_dimensions(word_counts)
    data = list(zip(fnames, word_counts))
    chunks = list(chunk(data, N_CHUNKS))
    print(chunks)


main()
