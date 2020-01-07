# make mine sweeper map
# v1 - fill field on a fly


def mine_sweeper(bombs, num_rows, num_cols):
    mine_sweeper_field = []
    for i in range(0, num_rows):
        mine_sweeper_field.append([])
        for j in range(0, num_cols):
            positon = [i, j]
            if positon in bombs:
                mine_sweeper_field[i].append(-1)
            else:
                count = 0
                for x in range(i - 1, i + 2):
                    for y in range(j - 1, j + 2):
                        positon = [x, y]
                        if positon in bombs:
                            count += 1
                mine_sweeper_field[i].append(count)
    for i in mine_sweeper_field:
        print(i)


bombs_position = [[0, 0], [0, 1]]
rows_number = 3
cols_nuber = 4

mine_sweeper(bombs_position, rows_number, cols_nuber)
