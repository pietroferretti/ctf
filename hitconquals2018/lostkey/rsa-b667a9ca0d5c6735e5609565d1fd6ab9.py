#!/usr/bin/env python
from Crypto.Util.number import *
from gmpy import *
import os,sys

sys.stdin  = os.fdopen(sys.stdin.fileno(), 'r', 0)
sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)

def genKey():
  return (65077525198716906989052965786614429979101385047820291573756927516142783748452405669187206396817533029970309955206319939451091607544051607360431351391957318807046735081358340818056707254691294605803685305513689194131170185885956523125234941436889383531502154934519878069636129726612910571905094456729227274659, 660910227265, 11290650180808754341524847537552983396645512697953104864151364097289029639721195699505063147692672275424643558526805489101882093303884890353630506423384264819397583764056554372814233341960184442144715391200084537060834940101993272425138945172956630099729148784688264015161839954416908849304700874268576140401)
  ## FIXME
  p = getPrime(512)
  q = getPrime(512)
  n = p*q
  phi = (p-1)*(q-1)
  while True:
    e = getRandomInteger(40)
    if gcd(e,phi) == 1:
      d = int(invert(e,phi))
      return n,e,d

def calc(n,p,data):
  num = bytes_to_long(data)
  res = pow(num,p,n)
  return long_to_bytes(res).encode('hex')

def readFlag():
  flag = open('flag').read()
  assert len(flag) >= 50
  assert len(flag) <= 60
  # prefix = os.urandom(68)    # FIXME
  prefix = 'ee48de5f6fcc4e8cd6b1438c290cd5c01687a35ec0b769384d590b0cee655a67b43dece955ca9a228e247aaea92677381a84e2ffbb313f509ea1217e1f2882a165e4e0bd'.decode('hex')
  return prefix+flag

if __name__ == '__main__':
  n,e,d = genKey()
  flag =  calc(n,e,readFlag())
  print 'Here is the flag!'
  print flag
  for i in xrange(150):
    msg = raw_input('cmd: ')
    if msg[0] == 'A':
      m = raw_input('input: ')
      try:
        m = m.decode('hex')
        print calc(n,e,m)
      except:
        print 'no'
        exit(0)
    elif msg[0] == 'B':
      m = raw_input('input: ')
      try:
        m = m.decode('hex')
        print calc(n,d,m)[-2:]
      except:
        print 'no'
        exit(0)

