This is the submittable code for the assignment.
It does not execute on Hadoop. See report section 4 for details.

To run standalone, execute the following command on Linux/Mac:
python3 1_generate_vectors_from_fnames.py sport/*.txt | python3 2_get_centroids.py | python3 3_nearest_centroid_to_vector.py | python3 4_calculate_centroid_position.py

The inputs and outputs of the various files are illustrated below:
1_generate_vectors_from_fnames.py 
Input: 	[ list of file names ]
Output:	[ “KEY”, <vector_representing_file> for each file name ]

2_get_centroids.py
Input:	Multiple (“KEY”, vector) key-value pairs
Output:	Multiple (vector, centroids) key-value pairs

3_nearest_centroid_to_vector.py
Input:	(vector, centroids) key-value pairs
Output:	(centroid, vector) key-value pairs

4_calculate_centroid_position.py
Input:	Multiple (centroid, vector) key-value pairs
Output:	(original_centroid, new_centroid) key-value pair

While this code is not executable on Hadoop, the run.sh will run the commands in the specified order to demonstrate that we understand the process of executing mappers and reducers on hadoop.

The run.sh file does have several dependencies including the assumption that HADOOP_HOME has been added to the path file (.bashrc in our case). This code was also written to be executed on Hadoop 2.8.
