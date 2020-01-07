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
                                    if path2[0] == path1[1] and path3[0] == path2[1] and path4[0] == path3[1] and path1[0] == path4[1]:
                                        if ((diag(path1[0], path3[0]) == diag(path2[0], path4[0])) and (diag(path1[0], path1[1]) == diag(path3[0], path3[1]))and (diag(path2[0], path2[1]) == diag(path4[0], path4[1]))):
                                            if (diag(path1[0], path3[0]) > 0 and diag(path2[0], path4[0]) > 0 and diag(path1[0], path1[1]) > 0 and diag(path3[0], path3[1]) > 0 and diag(path2[0], path2[1]) > 0 and diag(path4[0], path4[1]) > 0):
                                                count += 1
                                                # print(path1, " ", path2, " ", path3, " ", path4, " ", count)

    return count / 24


def diag(dot1, dot2):
    return ((dot1[0] - dot2[0]) ** 2 + (dot1[1] - dot2[1]) ** 2)**(1 / 2)


def find_roads(dots):
    roads = []
    for i in range(0, len(dots)):
        roads.append([])
        for j in range(0, len(dots)):
            roads[i].append([])
            roads[i][j].append(dots[i])
            roads[i][j].append(dots[j])
    return roads


dots_list1 = [[0, 1], [1, 1], [1, 0], [0, 0]]
dots_list2 = [[0, 1], [1, 1], [2, 1], [0, 0], [1, 0], [2, 0]]
dots_list3 = [[0, 2], [1, 2], [2, 2], [0, 1],
              [1, 1], [2, 1], [0, 0], [1, 0], [2, 0]]
dots_list4 = [[0, 3], [1, 3], [2, 3], [0, 2], [1, 2], [
    2, 2], [0, 1], [1, 1], [2, 1], [0, 0], [1, 0], [2, 0]]

print(count_rectangles(dots_list1))
print(count_rectangles(dots_list2))
print(count_rectangles(dots_list3))
# print(count_rectangles(dots_list4))
