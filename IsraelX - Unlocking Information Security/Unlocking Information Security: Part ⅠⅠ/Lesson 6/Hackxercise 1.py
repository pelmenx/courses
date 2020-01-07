# In an imaginary protocol stack, the header structures are as follows:
#
# Layer 1 has the following structure:
# The first  4  bytes are the ID of the sender
# The next  4  bytes are the ID of the receiver
# The next  4  bytes are the size of the content (let's call it  𝑛 )
# The next  𝑛  bytes are the content
# Layer 2 has the following header and footer:
# The first  4  bytes are the session ID
# The last  4  bytes are a checksum of the message
# The middle bytes are the content
# Layer 3 has the following structure:
# The first  4  bytes are the message ID
# The rest of the bytes are the message
# here is a message captured on the wire, that was sent using this protocol stack.

# b'\x08\x00\x00\x00\xf6\x01\x00\x00\x24\x00\x00\x00\x03\x00\x00\x00\x0c\x00\x00\x00I think, therefore I am.\xca\xcd\x00\x00'

# Write a Python program to decode the captured message and print out the contents of the following fields:
# sender ID, message ID, message text, and the checksum.

# Note that all the IDs and numbers in the message are unsigned  4 -byte integers, encoded in little endian format.
# You need to print and submit them as normal (decimal) numbers.


from struct import *
packet = b'\x08\x00\x00\x00\xf6\x01\x00\x00\x24\x00\x00\x00\x03\x00\x00\x00\x0c\x00\x00\x00I think, therefore I am.\xca\xcd\x00\x00'

# Don't change the code until this line


def show_details(pack):

    sender_ID = pack[:4]
    pack = pack[4:]
    checksum = pack[-4:]
    pack = pack[4:-4]
    message_ID = pack[8:12]
    message = pack[12:]
    size_of_the_content = (len(message))
    print(size_of_the_content)
    print(unpack("i", sender_ID)[0])
    print(unpack("i", message_ID)[0])
    print(message.decode())
    print(unpack("i", checksum)[0])

    # pass # print sender ID (decimal), message ID (decimal), the actual message (readable english text), and its checksum (decimal)


show_details(packet)
