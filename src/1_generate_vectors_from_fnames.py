"""

IN:     filename_glob

OUT:    "key"    <vector>
        "key"    <vector>
        ...
"""
import sys
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer


def file_names():
    return sys.argv[1:]


def words(fname):
    with open(fname, 'rt') as f:
        return ' '.join([l for l in f.readlines()])


def vectorise(fname_words_dict):
    # https://stackoverflow.com/questions/15899861/efficient-term-document-matrix-with-nltk
    vec = CountVectorizer()
    X = vec.fit_transform(fname_words_dict.values())
    df = pd.DataFrame(X.toarray(),
                      columns=vec.get_feature_names(),
                      index=[i for i in fname_words_dict.keys()])  # set up the table
    return zip(fname_words_dict.keys(), df.as_matrix())


def main():
    fnames = file_names()
    d = {}
    for fname in fnames:
        d[fname] = words(fname)
    fnames_vectors = vectorise(d)
    for fname, vector in fnames_vectors:
        print(fname, end='\t')
        for n in vector:
            print(n, end=' ')
        print()


main()
