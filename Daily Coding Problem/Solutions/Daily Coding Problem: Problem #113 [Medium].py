# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Given a string of words delimited by spaces, reverse the words in string. For
# example, given "hello world here", return "here world hello"
#
# Follow-up: given a mutable string representation, can you perform this operation
# in-place?
#
#
# --------------------------------------------------------------------------------
#
#
def reverse_word(string):
    string = list(string)
    print(string)
    left = 0
    right = len(string) - 1
    while left < right:
        if string[left] == " " and string[right] == " ":
            string = string[right + 1:] + string[left:right + 1] + string[:left]
            left += 1
            right -= 1
        elif string[left] != " " and string[right] != " ":
            left += 1
            right -= 1
        elif string[left] == " " and string[right] != " ":
            right -= 1
        elif string[right] == " " and string[left] != " ":
            left += 1
    string = "".join(string)
    return string


print(reverse_word("hello world here"))
