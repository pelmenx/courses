# The function weak_md5 is a "weaker" version of MD5, using only the first 5 bytes of the MD5 hash.
# This means its hashing size is  𝑛=40  and it can be brute forced rather easily.

# Implement a function find_collisions that loops over all the possible strings until it finds an
# arbitrary collision - that is, two different strings whose hash is the same - and returns them (as a tuple).
from itertools import product
import hashlib


def weak_md5(s):
    result = hashlib.md5(s.encode())
    result=result.hexdigest()[:5]
    return result


def find_collisions(s1):
    hash1 = weak_md5(s1)
    alphabet = "qwertyuiopasdfghjklzxcvbnm"

    for i in range(0, len(alphabet)):
        product_list = list(product(alphabet, repeat=i))

        for i in range(0, len(product_list)):
            s2 = (''.join(map(str, product_list[i])))
            hash2 = weak_md5(s2)

            if (hash1 == hash2) and (s1 != s2):
                return (s1,s2)


string1 = "foo"
tuple_collisions = find_collisions(string1)
print(tuple_collisions)