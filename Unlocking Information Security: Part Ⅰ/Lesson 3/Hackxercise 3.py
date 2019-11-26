from itertools import product


def simple_hash(s):
    r = 7
    for c in s:
        r = (r * 31 + ord(c)) % 2 ** 16
    return r


def crack(s1):
    hash1 = simple_hash(s1)
    alphabet = "qwertyuiopasdfghjklzxcvbnm"

    for i in range(0, len(alphabet)):
        product_list = list(product(alphabet, repeat=i))

        for i in range(0, len(product_list)):
            s2 = (''.join(map(str, product_list[i])))
            hash2 = simple_hash(s2)

            if (hash1 == hash2) and (s1 != s2):
                return s2


string1 = "foo"
string2 = crack(string1)
print(string2)
