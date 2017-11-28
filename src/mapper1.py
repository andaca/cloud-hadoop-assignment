#!/usr/bin/env python3

import sys
import re
from datetime import datetime
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from glob import glob  # use this for windows, works fine on linux without glob
from sys import argv


def get_file_array():
    # https://stackoverflow.com/questions/12501761/passing-multple-files-with-asterisk-to-python-shell-in-windows
    # for filename in glob(argv[1]): # This is the windows way
    # args = sys.argv[1:] # This is the linux way
    # for filename in args:
    #    print("the filename")
    #    print(filename)

    return sys.argv[1:]


def get_docs_file_array(file_array):
    docs, fnames = [], []
    for fname in file_array:
        try:
            with open(fname, 'rt') as f:
                docs.append(' '.join(f.readlines()))
            fnames.append(fname)
        except Exception as e:
            with open('error.log', 'at') as f:
                f.write("{} :: Skipping file {} :: {}\n".format(
                    datetime.now(), fname, e))
    return docs, fnames


def get_df(docs, file_array):
    # Will also need to get rid of words with a leading underscore - they are useless
    # Maybe get word stems as well? - have link for that

    # https://stackoverflow.com/questions/15899861/efficient-term-document-matrix-with-nltk
    vec = CountVectorizer()
    X = vec.fit_transform(docs)
    df = pd.DataFrame(X.toarray(), columns=vec.get_feature_names(), index=[
                      i for i in file_array])  # set up the table
    #df.to_csv("test.csv", encoding='utf-8', index=True)
    return df


def print_output(df):
    # https://www.shanelynn.ie/select-pandas-dataframe-rows-and-columns-using-iloc-loc-and-ix/
    # that's taking the values from all the rows, excluding the first column
    int_values = df.values[:, 1:].tolist()
    filename_values = df.index.values.tolist()

    # Iterate over the list, make the output
    count = 0
    for i in int_values:
        # This will be what is outputted to the second mapper/reducer
        print(('key', (filename_values[count], i)))
        count += 1


def main():
    file_array = get_file_array()
    # a new file_array is returned because if any of the files result in thrown errors
    # we need to know which files were actually used
    docs, file_array = get_docs_file_array(file_array)
    df = get_df(docs, file_array)
    print_output(df)


main()
