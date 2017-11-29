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

def find_cols_to_delete(df):
    # add stopwords to the cols to drop
    headers = list(df)
    columns_to_drop = []
    index = 0
    for column in df:
        total_num = df[column].sum(axis=None) # sum the values in the columns
        if total_num <= 1: # if the total is <= 1 - if the word only appears in one document, add to drop list
            columns_to_drop.append(headers[index])
        index += 1
    return columns_to_drop

def drop_columns(df):
    # This is original df
    # output as csv
    # iterate over it, drop the cols
    # return the updated dataframe
    print("before")
    print(df)
    stopwords = ['i', 'in', 'the', 'if', 'or', 'it']
    columns_to_drop = find_cols_to_delete(df)
    headers = list(df)
    # if stopword is in headers, add to array
    for word in stopwords:
        if word in headers:
            columns_to_drop.append(word)

    for i in columns_to_drop:
        df = df.drop([str(i)], axis=1) # drop the columns

    print("after")
    print(df)
    return df


def vectorise(fname_words_dict):
    # https://stackoverflow.com/questions/15899861/efficient-term-document-matrix-with-nltk
    vec = CountVectorizer()
    X = vec.fit_transform(fname_words_dict.values())
    df = pd.DataFrame(X.toarray(),
                      columns=vec.get_feature_names(),
                      index=[i for i in fname_words_dict.keys()])  # set up the table
    df.to_csv("vector_table_before.csv", encoding='utf-8', index=True)
    # remove stopwords etc.
    df = drop_columns(df)
    df.to_csv("vector_table_after.csv", encoding='utf-8', index=True)
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
