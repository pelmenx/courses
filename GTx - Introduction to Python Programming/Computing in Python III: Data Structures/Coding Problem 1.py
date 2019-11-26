#Write a function called count_types. count_types
#should take as input a single string, and return a
#dictionary. In the dictionary, the keys should be
#types of characters, and the values should be the
#number of times each type of character appeared in
#the string.
#
#The types of characters that should be handled (and
#thus, the keys in the dictionary) are:
#
# - upper: the count of upper-case or capital letters
# - lower: the count of lower-case letters
# - punctuation: the count of punctuation characters.
#   You may assume this is limited to these punctuation
#   characters: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
# - space: the count of spaces
# - numeral: the count of numerals, 0123456789
#
#Note, however, that any type of character that does
#NOT appear in the string should not be in the dictionary
#at all.
#
#For example:
#
#count_characters("aabbccc") ->
# {"lower": 7}
#count_characters("ABC 123 doe ray me!") ->
# {"upper": 3, "lower": 8, "punctuation": 1, "space": 4, "numeral": 3}
#
#Because the first string has only lower-case letters,
#"lower" is the only key in the dictionary.
#
#HINT: If you're sing the ord() function, capitals of
#ordinals between 65 and 90; lower-case letters have
#ordinals between 97 and 122; numerals are between 48
#and 57; spaces are 32; all other numbers between 33
#and 126 are punctuations, and no character will have
#an ordinal outside that range.


#Write your function here!
def count_types(text):
    dictionary={}
    count_upper=0
    count_lower=0
    count_numeral=0
    count_space=0
    count_punctuation=0
    for character in text:
        if ord(character)>=65 and ord(character)<=90:
            count_upper+=1
        elif ord(character)>=97 and ord(character)<=122:
            count_lower+=1
        elif ord(character)>=48 and ord(character)<=57:
            count_numeral+=1
        elif ord(character)==32:
            count_space+=1
        elif ord(character)>=33 and ord(character)<=126:
            count_punctuation+=1
    if count_upper>0:
        dictionary["upper"]=count_upper
    if count_lower>0:
        dictionary["lower"]=count_lower
    if count_numeral>0:
        dictionary["numeral"]=count_numeral
    if count_space>0:
        dictionary["space"]=count_space
    if count_punctuation>0:
        dictionary["punctuation"]=count_punctuation
    return dictionary
#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print (although the order of the keys may vary):
#
#{"lower": 7}
#{"upper": 3, "lower": 8, "punctuation": 1, "space": 4, "numeral": 3}
print(count_types("aabbccc"))
print(count_types("ABC 123 doe ray me!"))



