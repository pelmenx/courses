# make mine sweeper map
# v2 - fill fill by adding 1 to position close to bomb in each iteration


def mine_sweeper(bombs, num_rows, num_cols):
    mine_sweeper_field = []
    for i in range(0, num_rows):
        mine_sweeper_field.append([])
        for j in range(0, num_cols):
            mine_sweeper_field[i].append(0)
    for i in range(0, num_rows):
        for j in range(0, num_cols):
            positon = [i, j]
            if positon in bombs:
                mine_sweeper_field[i][j] = -1
                for x in range(i - 1, i + 2):
                    for y in range(j - 1, j + 2):
                        if 0 <= x < num_rows and 0 <= y < num_cols:
                            if mine_sweeper_field[x][y] != -1:
                                mine_sweeper_field[x][y] += 1
    for i in mine_sweeper_field:
        print(i)


bombs_position = [[0, 0], [0, 1]]
rows_number = 3
cols_nuber = 4

mine_sweeper(bombs_position, rows_number, cols_nuber)
