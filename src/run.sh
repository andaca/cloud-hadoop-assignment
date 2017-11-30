#!/bin/bash

# This file will call all of the other files

## First map_reduce job
run_map_reduce1() {
	$HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.8.2.jar \
	-mapper 1_generate_vectors_from_fnames.py \
	-reducer 2_get_centroids.py \
	-input test_files/*.txt -output map_reduce1_out/
}


# Second map_reduce job
run_map_reduce2() {
	$HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.8.2.jar \
	-mapper 3_nearest_centroid_to_vector.py \
	-reducer 4_calculate_centroid_position.py \
	-input map_reduce1_out/ -output map_reduce2_out/
}

# Method to check if the centroid has moved or not - calles the python function to do this
# Passes in the output of the firt map_reduce
check_distance() {
	# make copy of the part-00000 file to the main folder so it doesn't get deleted later on
	cp map_reduce1_out/part-00000 .
	has_moved.py map_reduce1_out/part-00000
}

final_run() {
	run_map_reduce1
	cat map_reduce1_out/part-0000 | python3 3_nearest_centroid_to_vector.py >> final_output.txt
}

run_map_reduce3(){
	$HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.8.2.jar \
	-mapper 1_generate_vectors_from_fnames.py \
	-reducer 2_get_centroids.py \
	-input part-00000 -output map_reduce2_out/
}



main() {
	run_map_reduce1
	run_map_reduce2
	run=true
	while [ $run == true ]; do
		# do a check, if check_distance returns true, go back to step 1 but run mr3 then mr4
		if check_distance; then
			# remove the original output directories
			rm -rf map_reduce1_out
			rm -rf map_reduce2_out
			run_map_reduce3
			run_map_reduce2
		else
			run=false
		fi
	done

}

main

# eliminate the useless keywords and be left with small dimensions