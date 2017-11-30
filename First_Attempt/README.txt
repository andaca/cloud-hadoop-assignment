The following code corresponds to section 3 of the report. This code is not executable on git but can be run standalone on the terminal of a Unix system using the following command:

python3 mapper.py sport/5*.txt | python3 k_means.py

Mapper.py:
Reads in the files and displays them as a table of term vectors. Uses Principal Component Analysis to reduce the document space.

K-Means.py:
This is the reducer. It takes in the output of the mapper and runs a K-Means algorithm on the data and outputs the clusters to the terminal.