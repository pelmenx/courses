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


def queens_position(n):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(n):
            matrix[i].append(5)

    tmp_matrix = copy.deepcopy(matrix)
    counter = 0
    for i in range(0, len(tmp_matrix)):
        for j in range(0, len(tmp_matrix[i])):
            if tmp_matrix[i][j] == 5:
                counter += 1
                for k in range(len(tmp_matrix[i])):
                    tmp_matrix[i][k] = 0
                    tmp_matrix[k][j] = 0
                start = [i - min(i, j), j - min(i, j)]
                for m in range(0, n - max(start)):
                    tmp_matrix[start[0] + m][start[1] + m] = 0
                for q in range(len(tmp_matrix)):
                    for w in range(len(tmp_matrix[i])):
                        if q + w == i + j:
                            tmp_matrix[q][w] = 0
                tmp_matrix[i][j] = 1
            for item in tmp_matrix:
                print(item)
            print("----------------------------", i, j, counter)


queens_position(3)
