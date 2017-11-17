from ecxor_handout_100 import *
from xortools3 import findkey

def str2bytes(s):
    return b''.join(ord(char).to_bytes(1, 'little') for char in s)

def bytes2str(b):
    return ''.join(chr(x) for x in b)

def encfunc(plain_char, key_char):
    return encrypt(str2bytes(key_char), plain_char)

# prepare lookup tables for fast decryption
print('Preparing lookup dictionary...')
dec_table = {}
for plain_i in range(256):
    print(plain_i)
    plain_char = chr(plain_i)
    for key_i in range(256):
        key_char = chr(key_i)
        cipher_char = bytes2str(encfunc(plain_char, key_char))
        if cipher_char not in dec_table:
            dec_table[(cipher_char, key_char)] = plain_char

def decfunc(ciphertext_char, key_char):
    return dec_table.get((ciphertext_char, key_char), '\xff')

with open('ciphertext') as f:
    ct = f.read()[8:-2]
ct_list = ct.split(';')

print('Finding best key...')
key = findkey(ct_list, keylen=12, decfunc=decfunc, verbose=True)

print('')
print('Plaintext:')
print(decrypt(str2bytes(key), str2bytes(ct)))