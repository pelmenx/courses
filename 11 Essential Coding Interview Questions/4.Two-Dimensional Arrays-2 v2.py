# show mine_sweeper map after click at certain cell
# if click was in safity field - show all opened cells
# else - show the original field
# v2-shows in Breadth-first Search, by checking close 9 cell and added them to que if they are safity


def fill_field(mine_sweeper_field, num_rows, num_cols, i_click, j_click, que, pointer=0):
    for i in range(que[pointer][0] - 1, que[pointer][0] + 2):
        for j in range(que[pointer][1] - 1, que[pointer][1] + 2):
            if 0 <= i < num_rows and 0 <= j < num_cols:
                if mine_sweeper_field[i][j] == 0:
                    que.append([i, j])
                    mine_sweeper_field[i][j] = -2
    pointer += 1
    if pointer < len(que):
        fill_field(mine_sweeper_field, num_rows,
                   num_cols, i_click, j_click, que, pointer)


def click(mine_sweeper_field, num_rows, num_cols, i_click, j_click):
    if mine_sweeper_field[i_click][j_click] == 0:
        mine_sweeper_field[i_click][j_click] = -2
        que = [[i_click, j_click]]
        fill_field(mine_sweeper_field, num_rows,
                   num_cols, i_click, j_click, que)
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
