# Implement Caesar’s cipher: implement a function encrypt that given a plaintext string and a key  𝑘
# (how many letters to shift), returns a ciphertext where each character is shifted  𝑘  places.
# (You can assume all characters are lowercase letters, with no punctuation or spaces.)


def encrypt(plaintext, k):
    alphabet_list = []
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    for letter in alphabet:
        alphabet_list.append(letter)

    plaintext_list = []

    for letter in plaintext:
        plaintext_list.append(letter)

    cyphertext_list = []
    for i in range(0, len(plaintext_list)):
        index = alphabet_list.index(plaintext_list[i])
        cyphertext_list.append(alphabet_list[(index + k) % 26])
    result = ''.join(map(str, cyphertext_list))
    return result


text = "a"
key = 5
cipertext = encrypt(text, key)
print(cipertext)
