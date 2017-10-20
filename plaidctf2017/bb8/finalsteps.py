# coding: utf-8
from Crypto.Cipher import AES
import pickle
bob_message = pickle.load(open('bobmessage', 'r'))
bob_message
len(bob_message)
len(bob_message)/32
bob_key = pickle.load(open('bobkey', 'r'))
bob_key
obj = AES.new('\xff'*16, AES.MODE_EBC)
obj = AES.new('\xff'*16, AES.MODE_ECB)
bob_message.encode('ascii')
bob_message.decode('ascii')
bob_message.decode('hex')
obj.decrypt(bob_message.decode('hex'))
alice_message = pickle.load(open('alicemessage', 'r'))
alice_message
alice_key = pickle.load(open('alicekey', 'r'))
alice_key
''.join('0' for x in alice_key if x=='-1' else '1')
''.join(['0' for x in alice_key if x=='-1' else '1'])
l = ''
for x in alice_key:
    if x == -1:
        l += '0'
    else:
        l += '1'
        
l
len(l)
l[1::2]
l[1::2][128]
l[1::2][:128]
a_key = l[1::2][:128]
len(a_key
)
a_key.decode('binary')
a_key.decode('bin')
key = ''
for i in range(len(a_key)/8):
    key += chr(int(a_key[8*i:8*i+8], 2))
    
key
len(key)
a_key[0:8]
obj2 = AES.new(key, AES.MODE_ECB)
obj2.decrypt(alice_message)
obj2.decrypt(alice_message.decode('hex'))
alice_flag = obj2.decrypt(alice_message.decode('hex'))
bob_flag = obj.decrypt(bob_message.decode('hex'))
flag = alice_flag + bob_flag
flag
flag = alice_flag.strip() + bob_flag.strip()
flag

# PCTF{perhaps_secrecy_aint_the_same_thing_as_authentication}
