# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Facebook.
#
# Implement regular expression matching with the following special characters:
#
#  * . (period) which matches any single character
#  * * (asterisk) which matches zero or more of the preceding element
#
# That is, implement a function that takes in a string and a valid regular
# expression and returns whether or not the string matches the regular expression.
#
# For example, given the regular expression "ra." and the string "ray", your
# function should return true. The same regular expression on the string "raymond"
# should return false.
#
# Given the regular expression ".*at" and the string "chat", your function should
# return true. The same regular expression on the string "chats" should return
# false.
#
#
# --------------------------------------------------------------------------------
#
#
def regexp_validator(regexp, string):
    #print(regexp, string)
    if regexp[0] != "*":
        if len(regexp) == 1:
            if len(string) == 1:
                return True
            else:
                return False
        if regexp[0] == string[0] or regexp[0] == ".":
            return regexp_validator(regexp[1:], string[1:])
    else:
        pass


print(regexp_validator("ra.", "ray"))
print(regexp_validator("ra.", "raymond"))
print(regexp_validator(".*at", "chat"))
print(regexp_validator(".*at", "chats"))
