1. Order the grainID_n.txt/orientations_n.txt properly.
2. Make Dream3D files over all the grainID_n.txt/orientations_n.txt files by Dream3D pipeline
3. Read 3D np array (grainIDs) from the Dream3D files and duplicate the array by 3x3x3 (np.tile) and re-write the grainID_n.txt
4. Re-do the 2. by the re-written grainID_n.txt 4.
5. From the result of 5., make the networkx graph.