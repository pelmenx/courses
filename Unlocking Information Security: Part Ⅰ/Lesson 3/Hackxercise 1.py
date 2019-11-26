#Use codeboard and the standard library hashlib module to compute the MD5, SHA1 and
# SHA256 (that's SHA2 with a hash size of  𝑛=256 ) of the string "Hello, world!".
import hashlib

# Your code here.

#md5
print(hashlib.md5(b"Hello, world!").hexdigest())
#sha1
print(hashlib.sha1(b"Hello, world!").hexdigest())
#sha256
print(hashlib.sha256(b"Hello, world!").hexdigest())