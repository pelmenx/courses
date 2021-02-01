# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Facebook.
#
# Given a string and a set of delimiters, reverse the words in the string while
# maintaining the relative order of the delimiters. For example, given
# "hello/world:here", return "here/world:hello"
#
# Follow-up: Does your solution work for the following cases: "hello/world:here/",
# "hello//world:here"
#
#
# --------------------------------------------------------------------------------
#
#
def reverse_word(string):
    delimiters = ":/"
    string = list(string)
    print(string)
    left = 0
    right = len(string) - 1
    while left < right:
        if string[left] in delimiters and string[right] in delimiters:
            string = string[right + 1:] + string[left:right + 1] + string[:left]
            left += 1
            right -= 1
        elif string[left] not in delimiters and string[right] not in delimiters:
            left += 1
            right -= 1
        elif string[left] in delimiters and string[right] not in delimiters:
            right -= 1
        elif string[right] in delimiters and string[left] not in delimiters:
            left += 1
    string = "".join(string)
    return string


print(reverse_word("hello//world:here"))
