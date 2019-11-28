# Write a XOR cipher: implement a function encrypt that given a plaintext string and a key  𝑘
# (also a string), returns a ciphertext where each character is XORed with its respective character in  𝑘 .
# Assume that the plaintext and key have the same length. (that is, plaintext[i] is XORed with k[i]).


def to_bin(string):
    string_binary = bytes(string, 'utf-8')
    string_binary_list = []
    for i in string_binary:
        string_binary_list.append(bin(i)[2:].zfill(8))
    return string_binary_list


def encrypt(plaintext, k):
    plaintext_binary_list = to_bin(plaintext)
    k_binary_list = to_bin(k)

    result_list = []

    for x, y in zip(plaintext_binary_list, k_binary_list):
        binary = ""
        for xx, yy in zip(x, y):
            if int(xx) != int(yy):
                binary += "1"
            else:
                binary += "0"
        result_list.append(binary)

    result = ""

    for i in range(0, len(result_list)):
        result += chr(int(result_list[i], 2))

    return result


text = "1"
key = "a"
ciphertext = encrypt(text, key)
print(ciphertext)
