# is a and b one away string?
def is_one_away_strings(a, b):
    if len(a) == len(b):
        common_character_number = 0
        for i in range(0, len(a)):
            if a[i] == b[i]:
                common_character_number += 1
            else:
                if i + 1 - common_character_number == 2:
                    return False
        return True

    elif len(a) - len(b) == -1:
        pointer = 0
        for i in range(0, len(a)):
            if a[i] == b[pointer]:
                pointer += 1
            else:
                if a[i] == b[pointer + 1]:
                    pointer += 2
                else:
                    return False
        return True

    elif len(b) - len(a) == -1:
        pointer = 0
        for i in range(0, len(b)):
            if b[i] == a[pointer]:
                pointer += 1
            else:
                if b[i] == a[pointer + 1]:
                    pointer += 2
                else:
                    return False
        return True
    else:
        return False


s1a = "abcde"
s1b = "abfde"

s2a = "abcde"
s2b = "abde"

s3a = "xyz"
s3b = "xayz"
print(is_one_away_strings(s1a, s1b))
print(is_one_away_strings(s2a, s2b))
print(is_one_away_strings(s3a, s3b))
