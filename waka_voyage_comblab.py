# ENGSCI233: Lab - Combinatorics

# imports
from functions_comblab import *

# create network object
network = Network()
network.read_network('waka_voyage_network.txt')

# find the shortest distnace from taiwan to Hokianga
distance, path = shortest_path(network, 'Taiwan', 'Hokianga')

# display out the result
print(distance)
print(path)

# initialise the greatest_distance variable
greatest_distance = 0

# perform the algorithm to all possible pair of source_node and network.nodes
# find the far distance in the network among all shortest path founded
for source_node in network.nodes:
    for destination_node in network.nodes:
        d, p = shortest_path(network, source_node.name, destination_node.name)
        if d > greatest_distance:
            greatest_distance = d
            greatest_path = p

# display out the pair of locations in the network which is the furthest apart
print(greatest_distance)
print(greatest_path)

