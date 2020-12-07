# Write a function called find_median. find_median
# should take as input a string representing a filename.
# The file corresponding to that filename will be a list
# of integers, one integer per line. find_median should
# return the median of the numbers in the file.
#
# If there is an odd number of values in the file, then
# find_median will return the middle value from the numbers
# in the file after they're sorted.
#
# If there is an even number of values in the file, then
# find_median should return the average of the two middle
# values after they're sorted.
#
# For example, in the dropdown in the top left you'll find a
# file named FindMedianInput.txt. There are 19 numbers in
# this file, so the median is the value at index 10 after
# sorting them: 16.
#
# You may assume that all lines in the file will contain a
# positive integer (greater than 0). There may be duplicates.


# Write your function here!
def find_median(file_name):
    list_of_integer = []
    file = open("./GTx - Introduction to Python Programming/Computing in Python III: Data Structures/"+file_name, "r")
    for line in file:
        list_of_integer.append(int(line.strip()))
    list_of_integer.sort()
    if len(list_of_integer) % 2 == 0:
        median = (list_of_integer[int(len(list_of_integer)/2)] +
                  list_of_integer[int(len(list_of_integer)/2)-1])/2
    else:
        median = list_of_integer[int(len(list_of_integer)/2)]
    return median


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
#print: 16
print(find_median("FindMedianInput.txt"))
