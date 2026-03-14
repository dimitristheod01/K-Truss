# K-Truss
**Overview**

This Python project implements an algorithm to detect k-trusses in a graph. A k-truss is a subset of edges where each edge is part of at least (k-2) triangles formed by the nodes in the subset. This project was inspired by graph structures used in network analysis, similar to those studied in research on social and communication networks.

The program reads graph data from a text file and outputs the edges that belong to the maximum k-trusses for a given value of k.

**Features**

Reads graph data from a .txt file using adjacency lists.

Finds edges that participate in the maximum number of k-trusses.

Handles undirected graphs with integer nodes starting from 0.

Modular Python implementation with separate functions for clarity.

**Dataset**

Graph input files are stored in the data folder:

graph1.txt – small example graph

graph2.txt – larger example graph

Each line in the input file represents an edge between two nodes:

Example:
0 1
0 10
1 9

**How to Run**

1. Make sure your Python script (trusses.py) is in the same folder as the data folder.

2. Enter the filename (e.g., graph1.txt) and the k value when prompted:

Give the file: graph1.txt
Enter k: 3

The script will print all edges that belong to the maximum k-trusses, one per line:

(0, 1)
(1, 9)
(0, 9)
(8, 10)
(10, 16)
(8, 16)
