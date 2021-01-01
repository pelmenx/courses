# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Microsoft.
#
# You have an N by N board. Write a function that, given N, returns the number of
# possible arrangements of the board where N queens can be placed on the board
# without threatening each other, i.e. no two queens share the same row, column,
# or diagonal.
#
#
# --------------------------------------------------------------------------------
#
#
import copy


def queens_position(n, matrix=[], counter=None):
    if not matrix:
        matrix = []
        for i in range(n):
            matrix.append([])
            for j in range(n):
                matrix[i].append(None)
        tmp_matrix = copy.deepcopy(matrix)
        counter = 0
        return queens_position(n, tmp_matrix, counter)
    else:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] is None:
                    matrix[i][j] = 1
                    counter += 1
                    for k in range(len(matrix[i])):
                        if k != j:
                            matrix[i][k] = 0
                            matrix[k][j] = 0
        print(matrix)
        print

queens_position(8)
