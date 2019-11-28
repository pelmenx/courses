# Implement a hash function simple_hash that given a string s, computes its hash as follows:
# it starts with r = 7, and for every character in the string, multiplies r by 31, adds that character to r,
# and keeps everything modulo  2^16 .


def simple_hash(s):
    r = 7
    for c in s:
        r = (r * 31 + ord(c)) % 2 ** 16
    return r


string = "simple"
string_hash = simple_hash(string)
