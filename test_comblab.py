# ENGSCI233: Lab - Combinatorics

# imports
from functions_comblab import *


def test_search_value_negative_three():
    # create the tree object and assign values
    tree = Tree()
    tree.build(tree_tuple=('A', (('B', (('D', None), ('E', None), ('F', None))), ('C', (('G', None), ('H', None))))))
    tree.assign_values(val_dict={'A': 2, 'B': -1, 'D': 3, 'E': 0, 'F': -2, 'C': 1, 'G': -3, 'H': 4})

    # call your search algorithm for search_value of -3
    node_name = search(tree=tree, search_value=-3)

    assert(node_name == 'G')


def test_shortest_path_simple_A_to_F():
    # create network object
    network = Network()
    network.read_network('simple_network.txt')

    # run the shortest path algorithm
    distance, path = shortest_path(network, 'A', 'F')

    assert (distance == 7 and path == ['A','B','C','E','F'])