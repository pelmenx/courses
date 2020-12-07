# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Facebook.
#
# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the
# number of ways it can be decoded.
#
# For example, the message '111' would give 3, since it could be decoded as 'aaa',
# 'ka', and 'ak'.
#
# You can assume that the messages are decodable. For example, '001' is not
# allowed.
#
#
# --------------------------------------------------------------------------------
#
#
def encoder(encode_text):
    map = {"1": "a", "2": "b", "3": "c", "4": "d", "5": "e", "6": "f", "7": "g", "8": "h", "9": "i",
           "10": "j", "11": "k", "12": "l", "13": "m", "14": "n", "15": "o", "16": "p", "17": "q",
           "18": "r", "19": "s", "20": "t", "21": "u", "22": "v", "23": "w", "24": "x", "25": "y", "26": "z"}
    if len(encode_text) == 1:
        count = 1
        print(encode_text)
    elif len(encode_text) == 2:
        if int(encode_text) >= 1 and int(encode_text) <= 26:
            count = 2
            print(encode_text[0], encode_text[1])
            print(encode_text)
        else:
            count = 1
            print(encode_text)
    else:
        count = encoder(encode_text[1:])
        if int(encode_text[:2]) >= 1 and int(encode_text[:2]) <= 26:
            count += encoder(encode_text[2:])

    return count


print(encoder("1213"))
