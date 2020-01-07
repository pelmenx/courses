# show mine_sweeper map after click at certain cell
# if click was in safity field - show all opened cells
# else - show the original field
# v1 - show show numbers in that order (left,right,down,up)


def click(mine_sweeper_field, num_rows, num_cols, i_click, j_click):
    if mine_sweeper_field[i_click][j_click] == 0:
        mine_sweeper_field[i_click][j_click] = -2
        j = j_click - 1
        while j >= 0 and mine_sweeper_field[i_click][j] == 0:
            mine_sweeper_field[i_click][j] = -2
            j -= 1
        j = j_click + 1
        while j < num_cols and mine_sweeper_field[i_click][j] == 0:
            mine_sweeper_field[i_click][j] = -2
            j += 1
        for x in range(i_click + 1, num_rows):
            for y in range(0, num_cols):
                if mine_sweeper_field[x][y] == 0:
                    if y - 1 >= 0:
                        if mine_sweeper_field[x][y - 1] == -2:
                            mine_sweeper_field[x][y] = -2
                            break
                    for y1 in range(y - 1, y + 2):
                        if 0 <= y1 < num_cols:
                            if mine_sweeper_field[x - 1][y1] == -2:
                                mine_sweeper_field[x][y] = -2
                                break
        for x in range(i_click - 1, num_rows):
            for y in range(0, num_cols):
                if mine_sweeper_field[x][y] == 0:
                    if y - 1 >= 0:
                        if mine_sweeper_field[x][y - 1] == -2:
                            mine_sweeper_field[x][y] = -2
                            break
                    for y1 in range(y - 1, y + 2):
                        if 0 <= y1 < num_cols:
                            if mine_sweeper_field[x + 1][y1] == -2:
                                mine_sweeper_field[x][y] = -2
                                break
    for i in mine_sweeper_field:
        print(i)
    print()


field = [[0, 0, 0, 0, 0], [
    0, 1, 1, 1, 0], [0, 1, -1, 1, 0]]
rows_number = 3
cols_nuber = 5
i_coordinate = 0
j_coordinate = 1

click(field, rows_number, cols_nuber, i_coordinate, j_coordinate)

field = [[-1, 1, 0, 0], [
    1, 1, 0, 0], [0, 0, 1, 1], [0, 0, 1, -1]]
rows_number = 4
cols_nuber = 4
i_coordinate = 1
j_coordinate = 2
click(field, rows_number, cols_nuber, i_coordinate, j_coordinate)
