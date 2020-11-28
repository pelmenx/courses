def count_rectangles(array):
    road_table = find_roads(array)
    count = 0
    for pathes1 in road_table:
        for path1 in pathes1:
            for pathes2 in road_table:
                for path2 in pathes2:
                    for pathes3 in road_table:
                        for path3 in pathes3:
                            for pathes4 in road_table:
                                for path4 in pathes4:
                                    # create a chain
                                    if path2[0] == path1[1] and path3[0] == path2[1] and path4[0] == path3[1] and path1[0] == path4[1]:
                                        # opisite sides should be equal
                                        if length(path1) == length(path3) and length(path2) == length(path4):
                                            # sides length should be possitive
                                            if length(path1) > 0 and length(path2) > 0 and length(path3) > 0 and length(path4) > 0:
                                                # diagonals should be equal
                                                if diag(path1[0], path3[0]) == diag(path2[0], path4[0]):
                                                    # diagonals length shold be positive
                                                    if diag(path1[0], path3[0]) > 0 and diag(path2[0], path4[0]) > 0:
                                                        count += 1

    return count / 24


def diag(dot1, dot2):
    return ((dot1[0] - dot2[0]) ** 2 + (dot1[1] - dot2[1]) ** 2)**(1 / 2)


def length(line):
    return ((line[0][0] - line[1][0]) ** 2 + (line[0][1] - line[1][1]) ** 2)**(1 / 2)


def find_roads(dots):
    # return all possible roads for every dot
    roads = []
    for i in range(0, len(dots)):
        roads.append([])
        for j in range(0, len(dots)):
            roads[i].append([])
            roads[i][j].append(dots[i])
            roads[i][j].append(dots[j])
    return roads


dots_list1 = [[0, 1], [1, 1],
              [0, 0], [1, 0]]
dots_list2 = [[0, 2], [1, 2],
              [0, 1], [1, 1],
              [0, 0], [1, 0]]
dots_list3 = [[0, 2], [1, 2], [2, 2],
              [0, 1], [1, 1], [2, 1],
              [0, 0], [1, 0], [2, 0]]
dots_list4 = [[0, 3], [1, 3], [2, 3],
              [0, 2], [1, 2], [2, 2],
              [0, 1], [1, 1], [2, 1],
              [0, 0], [1, 0], [2, 0]]

print(count_rectangles(dots_list1))
print(count_rectangles(dots_list2))
print(count_rectangles(dots_list3))
# print(count_rectangles(dots_list4))
