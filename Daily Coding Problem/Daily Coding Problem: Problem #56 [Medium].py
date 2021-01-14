# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Given an undirected graph represented as an adjacency matrix and an integer k,
# write a function to determine whether each vertex in the graph can be colored
# such that no two adjacent vertices share the same color using at most k colors.
#
#
# --------------------------------------------------------------------------------
#
#

def can_color_graph(adjacency_matrix, k):
    max_adjacencies = 0
    for row in adjacency_matrix:
        max_adjacencies = max(max_adjacencies, sum(row))

    return k > max_adjacencies


adjacency_matrix_1 = [
    [0, 1, 0, 0, 1, 0],
    [1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 1],
    [1, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0],
]
print(can_color_graph(adjacency_matrix_1, 3))
