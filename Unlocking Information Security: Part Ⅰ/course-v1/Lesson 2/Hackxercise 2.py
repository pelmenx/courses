#Brute-force the following Caesar’s cipher, and find the plaintext and key of the following message:
#kyvtrmrcipnzccrkkrtbwifdkyvefikynvjkrkeffe
alphabet = "abcdefghijklmnopqrstuvwxyz"


def encrypt(plaintext, k):
    ciphertext = []
    for c in plaintext:
        i = alphabet.index(c)
        j = (i + k) % len(alphabet)
        ciphertext.append(alphabet[j])
    return ''.join(ciphertext)


def decrypt(ciphertext, k):
    return encrypt(ciphertext, -k)


def brute_force(ciphertext):
    for i in range(0, len(alphabet)):
        print(i, decrypt(ciphertext, i))


brute_force("kyvtrmrcipnzccrkkrtbwifdkyvefikynvjkrkeffe")