# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# You are given an M by N matrix consisting of booleans that represents a board.
# Each True boolean represents a wall. Each False boolean represents a tile you
# can walk on.
#
# Given this matrix, a start coordinate, and an end coordinate, return the minimum
# number of steps required to reach the end coordinate from the start. If there is
# no possible path, then return null. You can move up, left, down, and right. You
# cannot move through walls. You cannot wrap around the edges of the board.
#
# For example, given the following board:
#
# [[f, f, f, f],
# [t, t, f, t],
# [f, f, f, f],
# [f, f, f, f]]
#
#
# and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number
# of steps required to reach the end is 7, since we would need to go through (1,
# 2) because there is a wall everywhere else on the second row.
#
#
# --------------------------------------------------------------------------------
#
#
def find_way(matrix, start, end):
    global list
    if start == end:
        print("FINISH")
    if start not in list:
        tmp = []
        if 0 < start[0] < len(matrix) and 0 < start[1] + 1 < len(matrix[0]) and matrix[start[0]][start[1] + 1] == 0 and (start[0], start[1] + 1) not in list:
            tmp.append([start[0], start[1] + 1])
            print("Right")
        if 0 < start[0] < len(matrix) and 0 < start[1] - 1 < len(matrix[0]) and matrix[start[0]][start[1] - 1] == 0 and (start[0], start[1] - 1) not in list:
            tmp.append([start[0], start[1] - 1])
            print("Left")
        if 0 < start[0] + 1 < len(matrix) and 0 < start[1] < len(matrix[0]) and matrix[start[0] + 1][start[1]] == 0 and (start[0] + 1, start[1]) not in list:
            tmp.append([start[0] + 1, start[1]])
            print("Down")
        if 0 < start[0] - 1 < len(matrix) and 0 < start[1] < len(matrix[0]) and matrix[start[0] - 1][start[1]] == 0 and (start[0] - 1, start[1]) not in list:
            tmp.append([start[0] - 1, start[1]])
            print("Up")
    list[start] = tmp.copy()
    print(list)


matrix = [[0, 0, 0, 0],
          [1, 1, 0, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]

matri1 = [[0, 0, 0, 1],
          [1, 1, 0, 1],
          [0, 0, 0, 1],
          [1, 1, 1, 1]]

start = (2, 2)
end = (0, 0)

list = {}

find_way(matri1, start, end)
