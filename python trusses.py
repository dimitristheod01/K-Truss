import random
import re
#Ask User for file name
filename = input("Give a file: ")
f = open(f"data/{filename}", "r")  # file reading
k = int(input("Enter k: "))
l = f.readlines() # readlines returns the content of a file in a list 


# Function to remove trailing whitespace from each string in a list.

def remove_whitetrail(list):
    cleaned_list = []
    for i in range(len(list)):
        new = re.sub ("\s$","",list[i])
        cleaned_list.append(new)
    return cleaned_list

cleaned_list = remove_whitetrail(l)

#-------------------------------------------------------------------------------------------------
# Function to clean a list of strings by splitting each string based on whitespace characters and returning a list of lists where each inner list contains the node connections based of the original strings.  

def split_list(list):
    splitted_list = []
    for y in range (len(list)):
        new2 = re.split("\s", list[y])
        splitted_list.append(new2)
    return splitted_list

edges = split_list(cleaned_list)

#-------------------------------------------------------------------------------------------------
# Function to convert each element of a list of lists to integers.

def make_num(list):
    for j in range (len(list)):
        for c in range(2):
            list [j][c] = int(list[j][c])
    return list

edges = make_num(edges)

#-------------------------------------------------------------------------------------------------
# Function to convert each element of a list of lists to integers.

def make_tuple(list):
    for i,v in enumerate(list):
        list[i] = tuple(v)
    return list

edges = make_tuple(edges)

#-------------------------------------------------------------------------------------------------
# Function to find neighbors of a given node in a list of edges represented as pairs.
    
def neighbour (node):
    n = set()
    for i in range(len(edges)):
        if edges[i][0] == node: 
            n.add(edges[i][1]) 
        elif edges[i][1] == node:
             n.add(edges[i][0])
    return n

#-------------------------------------------------------------------------------------------------
# Create the k-truss algorithm function

def k_truss(graph,k):
    i=0  
    while  i < len(graph)-1:   
        for value in graph:
             if len(neighbour(value[0]).intersection(neighbour(value[1]))) < k-2:
                graph.remove(value)
        i+=1   
    return graph

print(k_truss(edges,k))


