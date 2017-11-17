from pwn import *
from lpn_chal import pack, deserialize_mat
import numpy as np

host = 'crypto.chal.csaw.io'
port = 1922

flag = ''
# try again until 'f' (the noise applied to the flag) has zero bits
while 'flag' not in flag:
    with remote(host, port) as conn:
        line = conn.recvline().split()[1][1:-1].replace('\\n','\n')
        A = deserialize_mat(line)
        line = conn.recvline().split()[1][1:-1].replace('\\n','\n')
        B = deserialize_mat(line)
        line = conn.recvline().split()[1][1:-1].replace('\\n','\n')
        u = deserialize_mat(line)
        line = conn.recvline().split()[1][1:-1].replace('\\n','\n')
        c = deserialize_mat(line)

        f = np.zeros((1600,),dtype=np.int)
        plain = (c + f.T.dot(B)) % 2
        flag = bytearray(pack(plain))

print(flag)