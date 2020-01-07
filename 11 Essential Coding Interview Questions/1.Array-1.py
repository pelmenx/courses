# find most frequent number in array


def most_frequent(given_array):
    frequent = {}
    count = 1
    for number in given_array:
        if number in frequent:
            frequent[number] += 1
            if frequent[number] > count:
                count += 1
                item = number
        else:
            frequent[number] = 1
    return item


array = [1, 3, 1, 2, 1]

print(most_frequent(array))
