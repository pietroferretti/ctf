#!/usr/bin/env python3
import os
from pycryptography import encrypt
from secret import flag


if __name__ == '__main__':
    with open('flag.enc', 'wb+') as f:
        # 160 bits security!
        enc = encrypt(flag.encode(), os.urandom(20))
        f.write(enc)
