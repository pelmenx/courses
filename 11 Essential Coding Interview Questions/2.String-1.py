# find first non repeating character
def non_repeating(string):
    number = -1
    frequent_dictionary = {}
    non_repeating_character = []
    for character in string:
        if character in frequent_dictionary:
            frequent_dictionary[character] += 1
            non_repeating_character.remove(character)
        else:
            frequent_dictionary[character] = 1
            non_repeating_character.append(character)
    if len(non_repeating_character) > 0:
        return non_repeating_character[0]
    else:
        return non_repeating_character


s1 = "aabcb"
s2 = "xxyz"
s3 = "aabb"
print(non_repeating(s1))
print(non_repeating(s2))
print(non_repeating(s3))
