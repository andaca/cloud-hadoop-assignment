#!/usr/bin/env python3

import sys
import re
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from glob import glob # use this for windows, works fine on linux without glob
from sys import argv

file_array = []
# https://stackoverflow.com/questions/12501761/passing-multple-files-with-asterisk-to-python-shell-in-windows
for filename in glob(argv[1]): # This is the windows way
#args = sys.argv[1:] # This is the linux way 
#for filename in args:
    print("the filename")
    print(filename)
    file_array.append(filename)

docs = []
count = 0
while count < len(file_array):
    file = open(file_array[count],"r")
    s = ""
    for line in file:
        s+=str(line)
    # https://stackoverflow.com/questions/39906519/remove-numbers-string-python
    string_no_numbers = re.sub("\d+", "", s) # maybe keep the numbers in and then reduce the table size by getting rid of numbers and stop words
    docs.append(string_no_numbers)
    file.close()
    count += 1

# Will also need to get rid of words with a leading underscore - they are useless
# Maybe get word stems as well? - have link for that

# https://stackoverflow.com/questions/15899861/efficient-term-document-matrix-with-nltk
vec = CountVectorizer()
X = vec.fit_transform(docs)
df = pd.DataFrame(X.toarray(), columns=vec.get_feature_names(), index=[i for i in file_array]) # set up the table
df.to_csv("term_vector_table.csv", encoding='utf-8', index=True)
#print(df)

# https://www.shanelynn.ie/select-pandas-dataframe-rows-and-columns-using-iloc-loc-and-ix/
int_values = df.values[:, 1:].tolist() # that's taking the values from all the rows, excluding the first column
filename_values = df.index.values.tolist()

# Iterate over the list, make the output
count = 0
for i in int_values:
    # This will be what is outputted to the second mapper/reducer
    print(('key',(filename_values[count],i)))
    count+=1

## ===========================================================================
## Old ideas
# Numpy .squeze could reduce dimensions?
# To run: mapper.py *.txt - windows
# To run: linux =  python3 mapper.py *.txt
# Might need to filter out _ in words as well

## ======================================================================================== ##

# Say that in Hadoop they divide on 64MB, so our solution isn't that size - therefore parallelisism 
# won't happen unless we split it ourselves. - say this in report.

# 128 MB in Hadoop

# simulated parallelism
# hadoop better for big data, time gain in splitting the data is gone in making it work

# Hadoop - every time you do a task, Hadoop keeps going to and from HDFS, reading from HDFS and writing to this every time which is time consuming.
# Small data, gaining by splitting data is gone then - not really worth it for small files.

# Just explain code for report and say why etc.
# Say used single node and why and how to run it, what version of Hadoop we used.
# Same key so the reducer can reduce it properly - principle of reducer is combining the same keys.

# Hadoop 2 uses yarn which is 128MB. Increase it to reduce the meta data - one namenode (in master) and multiple datanodes