# Write a function called are_anagrams. The function should
# have two parameters, a pair of strings. The function should
# return True if the strings are anagrams of one another,
# False if they are not.
#
# Two strings are considered anagrams if they have only the
# same letters, as well as the same count of each letter. For
# this problem, you should ignore spaces and capitalization.
#
# So, for us: "Elvis" and "Lives" would be considered
# anagrams. So would "Eleven plus two" and "Twelve plus one".
#
# Note that if one string can be made only out of the letters
# of another, but with duplicates, we do NOT consider them
# anagrams. For example, "Elvis" and "Live Viles" would not
# be anagrams.


# Write your function here!
def are_anagrams(string1, string2):
    string1 = string1.lower().replace(" ", "")
    string2 = string2.replace(" ", "").lower()
    print
    dic1 = {}
    dic2 = {}
    for i in string1:
        if i in dic1:
            dic1[i] += 1
        else:
            dic1[i] = 1

    for i in string2:
        if i in dic2:
            dic2[i] += 1
        else:
            dic2[i] = 1
    return dic1 == dic2


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: True, False, True, False, each on their own line.
print(are_anagrams("Elvis", "Lives"))
print(are_anagrams("Elvis", "Live Viles"))
print(are_anagrams("Eleven plus two", "Twelve plus one"))
print(are_anagrams("Nine minus seven", "Five minus three"))
