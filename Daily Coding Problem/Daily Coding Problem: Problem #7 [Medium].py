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
def encoder(encode_text, text=[], tmp_text1=[]):
    map = {"1": "a", "2": "b", "3": "c", "4": "d", "5": "e", "6": "f", "7": "g", "8": "h", "9": "i",
           "10": "j", "11": "k", "12": "l", "13": "m", "14": "n", "15": "o", "16": "p", "17": "q",
           "18": "r", "19": "s", "20": "t", "21": "u", "22": "v", "23": "w", "24": "x", "25": "y", "26": "z"}
    if len(encode_text) == 1:
        count = 1

        text.append(encode_text)
        tmp_text1.extend(text)
        text = tmp_text1
        print("!", text)
        for i in text:
            print(map[i], end='')
        print()
        text = []
    elif len(encode_text) == 2:
        if int(encode_text) >= 1 and int(encode_text) <= 26:
            count = 2

            tmp_text = text.copy()
            text.append(encode_text[0])
            text.append(encode_text[1])
            print("@", text)
            for i in text:
                print(map[i], end='')
            print()
            text = []
            text.extend(tmp_text)
            text.append(encode_text)
            print("#", text)
            for i in text:
                print(map[i], end='')
            print()
            text = []
        else:
            count = 1

            print(encode_text)
            text.append(encode_text[0])
            text.append(encode_text[1])
            print("%", text)
            for i in text:
                print(map[i], end='')
            print()
            text = []
    else:

        tmp_text1 = text.copy()
        text.append(encode_text[:1])
        count = encoder(encode_text[1:], text, tmp_text1)
        text = []
        if int(encode_text[:2]) >= 1 and int(encode_text[:2]) <= 26:
            text.append(encode_text[:2])
            count += encoder(encode_text[2:], text, tmp_text1)

    return count


print(encoder("1213"))
