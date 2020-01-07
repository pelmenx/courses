# rotate the array to 90 degree
def rotate(given_array, n, i, y):
    given_array[i][y], given_array[y][n] = given_array[y][n], given_array[i][y]
    given_array[i][y], given_array[n][n -
                                      y + i] = given_array[n][n - y + i], given_array[i][y]
    given_array[i][y], given_array[n -
                                   y + i][i] = given_array[n - y + i][i], given_array[i][y]


def rotation(given_array, n):
    inner_square_number = n // 2
    n = n - 1
    for i in range(0, inner_square_number):
        for y in range(i, n):
            rotate(given_array, n, i, y,)
        n = n - 1

    for i in given_array:
        print(i)
    print()


# array = [[1, 2, 3], [
# 4, 5, 6], [7, 8, 9]]
# n = len(array)

# rotation(array, n)

# array = [[11, 12, 13, 14], [15, 16, 17, 18], [19, 20, 21, 22], [23, 24, 25, 26]]
# n = len(array)

# rotation(array, n)

array = [[11, 12, 13, 14, 15, 16], [21, 22, 23, 24, 25, 26], [
    31, 32, 33, 34, 35, 36], [41, 42, 43, 44, 45, 46], [51, 52, 53, 54, 55, 56], [61, 62, 63, 64, 65, 66]]
n = len(array)
rotation(array, n)
