# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Given an array of strictly the characters 'R', 'G', and 'B', segregate the
# values of the array so that all the Rs come first, the Gs come second, and the
# Bs come last. You can only swap elements of the array.
#
# Do this in linear time and in-place.
#
# For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should
# become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].
#
#
# --------------------------------------------------------------------------------
#
#
def segregation(list):
    pointer = 0
    right = len(list) - 1
    left = 0
    while pointer <= right:
        if list[pointer] == "R":
            if pointer == left:
                pointer += 1
            else:
                tmp_1 = list[pointer]
                tmp_2 = list[left]
                list[pointer] = tmp_2
                list[left] = tmp_1
                left += 1
        elif list[pointer] == "B":
            if pointer == right:
                pointer += 1
            else:
                tmp_1 = list[pointer]
                tmp_2 = list[right]
                list[pointer] = tmp_2
                list[right] = tmp_1
                right -= 1
        else:
            pointer += 1
    return list


print(segregation(['G', 'R']))
print(segregation(['G', 'B', 'R']))
print(segregation(['B', 'G', 'R']))
print(segregation(['G', 'B', 'R', 'R', 'B', 'R', 'G']))
