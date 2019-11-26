#Write the stream cipher fake-RC4: implement a function encrypt that given a plaintext and a 32-bytes key  𝑘 ,
# returns a ciphertext encrypted with a weak variant of RC4 which we describe here.

#First, implement the fake-RC4 pseudo-random generator (PRG):

#It starts with  𝑖=𝑗=0 , and to generate the next byte in the keystream it:
#Increments  𝑖  by  1  (modulo the length of the key),
#Increments  𝑗  by the  𝑖−𝑡ℎ  character of the key (module the length of the key),
#Swaps the  𝑖−𝑡ℎ  character of the key with its  𝑗−𝑡ℎ  character,
#Adds the  𝑖−𝑡ℎ  character of the key and its  𝑗−𝑡ℎ  character, modulo the length of the key,
# and returns the key's character at that index.
#So for example, if the  𝑖−𝑡ℎ  character of the key was 'a' (whose ASCII value is 97),
#and its  𝑗−𝑡ℎ  character was '3' (whose ASCII value is 51), their sum would be 148. Since the key length is 32,
#the result will be  148%32=20 , so the pseudo random generator would return the  20−𝑡ℎ  character of the key as the next byte.

#Once you have the pseudo-random generator working, the rest is easy:

#Iterate over the plaintext
#XOR every character with the next byte of the pseudo-random generator's keystream
#Return the result as the ciphertext!

def get_prg(plaintext, k):
    k = list(k)
    i = 0
    j = 0

    keystream = []
    for x in range(0, len(plaintext)):
        i = (i + 1) % 32
        j = (j + int(k[i])) % 32
        k[i], k[j] = k[j], k[i]

        keystream.append(k[int(k[i]) + int(k[j]) % 32])

    keystream = ''.join(map(str, keystream))
    return fake_rc4(plaintext, keystream)


def fake_rc4(plaintext, k):
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


def to_bin(string):
    string_binary = bytes(string, 'utf-8')
    string_binary_list = []
    for i in string_binary:
        string_binary_list.append(bin(i)[2:].zfill(8))
    return string_binary_list


text = "qwe"
key = "12345678901234567890123456789012"
ciphertext = get_prg(text, key)
print(ciphertext)
