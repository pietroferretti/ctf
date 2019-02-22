# coding: utf-8
import requests
bank = 'badc7c2da792e765fd572599b187a055'
address = '0x4836D27fC5397854Db3eEc3BefEAb299cA19338f'
api = 'http://35.207.136.0/bank/eth/'
req = 
    'jsonrpc': '2.0',
    'method': 'eth_getLogs',
    'params': [
      {
        'address': bank_address,
        'fromBlock': '0x0',
        'toBlock': 'latest'
      }
    ],
    'id': 0
  };
req = {'jsonrpc': '2.0',
    'method': 'eth_getLogs',
    'params': [
      {
        'address': bank_address,
        'fromBlock': '0x0',
        'toBlock': 'latest'
      }
    ],
    'id': 0
  };
req = {'jsonrpc': '2.0',
    'method': 'eth_getLogs',
    'params': [
      {
        'address': address,
        'fromBlock': '0x0',
        'toBlock': 'latest'
      }
    ],
    'id': 0
  };
res = requests.post(api + bank, json=req)
res.text
api + bank
res = requests.post('http://35.207.136.0/eth/' + bank, json=req)
api + bank
res.text
api = 'http://35.207.136.0/eth/'
def doreq(req):
    global bank
    res = requests.post(api + bank, json=req)
    return res
r = doreq(req)
r
r.text
req = {'jsonrpc': '2.0',
    'method': 'eth_accounts',
    'params':[]
    'id': 0
  };
req = {'jsonrpc': '2.0',
    'method': 'eth_accounts',
    'params':[],
    'id': 0
  };
r = doreq(req)
r.text
bank = '7694e1397836ad7b04da0a67b5de4878'
req = {'jsonrpc': '2.0',
    'method': 'eth_getCode',
    'params':[address, 'latest'],
    'id': 0
  };
r = doreq(req)
r.text
from hashlib import sha3
from hashlib import sha384
sha384
help(sha384)
'627a7a723058'.decode('hex')
req = {'jsonrpc': '2.0',
    'method': 'eth_getStorageAt',
    'params': [address, 0x64, 'latest'],
    'id': 0
  };
r = doreq(req)
r.text
bank = '8b3a40c41e29154f88c6472c3bbc0209'
r = doreq(req)
r.text
req = {'jsonrpc': '2.0',
    'method': 'eth_getStorageAt',
    'params': [address, 0x65, 'latest'],
    'id': 0
  };
r = doreq(req)
r.text
req = {'jsonrpc': '2.0',
    'method': 'eth_getStorageAt',
    'params': [address, 0x0, 'latest'],
    'id': 0
  };
doreq(req).text
req = {'jsonrpc': '2.0',
    'method': 'eth_getStorageAt',
    'params': [address, 0x1, 'latest'],
    'id': 0
  };
doreq(req).text
0x64
req = {'jsonrpc': '2.0',
    'method': 'eth_getStorageAt',
    'params': [address, 0x64, 'latest'],
    'id': 0
  };
doreq(req).text
bank = 'd319c6fa98123460e7dd4e6df4ca7ace'
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
doreq(req).text
doreq(req).text
doreq(req).text
doreq(req).text
def getcoinbase():
    global bank
    req = {
        'jsonrpc': '2.0',
        'method': 'eth_coinbase',
        'params': [],
        'id': 0
    }
    return doreq(req).text
bank = '304eeaecf67a3d578114c3a623fbf20b'
getcoinbase()
import json
def getcoinbase():
    global bank
    req = {
        'jsonrpc': '2.0',
        'method': 'eth_coinbase',
        'params': [],
        'id': 0
    }
    return json.loads(doreq(req).text)['result']
getcoinbase()
coinbase = getcoinbase()
req = {
	"jsonrpc" : "2.0",
	"method" : "eth_sendTransaction",
	"params" : [{
			"from" : "0xcd2a3d9f938e13cd947ec05abc7fe734df8dd826",
			"data" : "6060604052341561000c57fe5b5b6101598061001c6000396000f30060606040526000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff168063cfae32171461003b575bfe5b341561004357fe5b61004b6100d4565b604051808060200182810382528381815181526020019150805190602001908083836000831461009a575b80518252602083111561009a57602082019150602081019050602083039250610076565b505050905090810190601f1680156100c65780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b6100dc610119565b604060405190810160405280600381526020017f486921000000000000000000000000000000000000000000000000000000000081525090505b90565b6020604051908101604052806000815250905600a165627a7a72305820ed71008611bb64338581c5758f96e31ac3b0c57e1d8de028b72f0b8173ff93a10029"
		}
	],
	"id" : 1
}
req
req = {
	"jsonrpc" : "2.0",
	"method" : "eth_sendTransaction",
	"params" : [{
			"from" : coinbase,
			"data" : "6060604052341561000c57fe5b5b6101598061001c6000396000f30060606040526000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff168063cfae32171461003b575bfe5b341561004357fe5b61004b6100d4565b604051808060200182810382528381815181526020019150805190602001908083836000831461009a575b80518252602083111561009a57602082019150602081019050602083039250610076565b505050905090810190601f1680156100c65780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b6100dc610119565b604060405190810160405280600381526020017f486921000000000000000000000000000000000000000000000000000000000081525090505b90565b6020604051908101604052806000815250905600a165627a7a72305820ed71008611bb64338581c5758f96e31ac3b0c57e1d8de028b72f0b8173ff93a10029"
		}
	],
	"id" : 1
}
doreq(req).text
t = doreq(req).text
print(t)
json.loads(t)['error']
json.loads(t)['error']
json.loads(t)['error']['data']
json.loads(t)['error']['data']['0xe9c5b973424746c563a04fff66e0cb15107b2167f59c12077e8d00915dba8308']
json.loads(t)['error']['data']['stack']
print json.loads(t)['error']['data']['stack']
req = {'jsonrpc': '2.0',
    'method': 'eth_getBalance',
    'params': [coinbase, 'latest'],
    'id': 0
  };
doreq(req).text
req = {
	"jsonrpc" : "2.0",
	"method" : "eth_sendTransaction",
	"params" : [{
			"from" : coinbase,
			"data" : "6060604052341561000c57fe5b5b6101598061001c6000396000f30060606040526000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff168063cfae32171461003b575bfe5b341561004357fe5b61004b6100d4565b604051808060200182810382528381815181526020019150805190602001908083836000831461009a575b80518252602083111561009a57602082019150602081019050602083039250610076565b505050905090810190601f1680156100c65780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b6100dc610119565b604060405190810160405280600381526020017f486921000000000000000000000000000000000000000000000000000000000081525090505b90565b6020604051908101604052806000815250905600a165627a7a72305820ed71008611bb64338581c5758f96e31ac3b0c57e1d8de028b72f0b8173ff93a10029",
'gas':10000000000
		}
	],
	"id" : 1
}
doreq(req).text
req = {
	"jsonrpc" : "2.0",
	"method" : "eth_sendTransaction",
	"params" : [{
			"from" : coinbase,
			"data" : "6060604052341561000c57fe5b5b6101598061001c6000396000f30060606040526000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff168063cfae32171461003b575bfe5b341561004357fe5b61004b6100d4565b604051808060200182810382528381815181526020019150805190602001908083836000831461009a575b80518252602083111561009a57602082019150602081019050602083039250610076565b505050905090810190601f1680156100c65780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b6100dc610119565b604060405190810160405280600381526020017f486921000000000000000000000000000000000000000000000000000000000081525090505b90565b6020604051908101604052806000815250905600a165627a7a72305820ed71008611bb64338581c5758f96e31ac3b0c57e1d8de028b72f0b8173ff93a10029",
'gas':10000000
		}
	],
	"id" : 1
}
doreq(req).text
req = {
	"jsonrpc" : "2.0",
	"method" : "eth_sendTransaction",
	"params" : [{
			"from" : coinbase,
			"data" : "6060604052341561000c57fe5b5b6101598061001c6000396000f30060606040526000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff168063cfae32171461003b575bfe5b341561004357fe5b61004b6100d4565b604051808060200182810382528381815181526020019150805190602001908083836000831461009a575b80518252602083111561009a57602082019150602081019050602083039250610076565b505050905090810190601f1680156100c65780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b6100dc610119565b604060405190810160405280600381526020017f486921000000000000000000000000000000000000000000000000000000000081525090505b90565b6020604051908101604052806000815250905600a165627a7a72305820ed71008611bb64338581c5758f96e31ac3b0c57e1d8de028b72f0b8173ff93a10029",
'gas':100000
		}
	],
	"id" : 1
}
doreq(req).text
req = {
	"jsonrpc" : "2.0",
	"method" : "eth_sendTransaction",
	"params" : [{
			"from" : coinbase,
			"data" : "6060604052341561000c57fe5b5b6101598061001c6000396000f30060606040526000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff168063cfae32171461003b575bfe5b341561004357fe5b61004b6100d4565b604051808060200182810382528381815181526020019150805190602001908083836000831461009a575b80518252602083111561009a57602082019150602081019050602083039250610076565b505050905090810190601f1680156100c65780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b6100dc610119565b604060405190810160405280600381526020017f486921000000000000000000000000000000000000000000000000000000000081525090505b90565b6020604051908101604052806000815250905600a165627a7a72305820ed71008611bb64338581c5758f96e31ac3b0c57e1d8de028b72f0b8173ff93a10029",
'gas':1000000
		}
	],
	"id" : 1
}
doreq(req).text
def buildreq(method, params)
def buildreq(method, params):
    return {
        'jsonrpc': '2.0',
        'method': method,
        'params': params,
        'id': 0
    }
def isowner(addr):
    req = buildreq('eth_sendTransaction', [{'from': getcoinbase(), 'data': '0'*2*0x20, 'to':bank}])
    return doreq(req).text 
bank = '54cc0958f8674377aa2a9ef297a6a067'
isowner(0)
bank
def isowner(addr):
    req = buildreq('eth_sendTransaction', [{'from': getcoinbase(), 'data': '0'*2*0x20, 'to':address}])
    return doreq(req).text 
isowner(0)
address
def isowner(addr):
    req = buildreq('eth_sendTransaction', [{'from': getcoinbase(), 'data': "0x2f54bf6e000000000000000000000000" + hex(int(addr, 16))[:2].strip('L').rjust(0x20, '0'), 'to':address}])
    return doreq(req).text 
isowner(getcoinbase())
bank = 'adc096d41fd522e20bd53d613bd045e9'
isowner(getcoinbase())
req = buildreq('eth_sendTransaction', [{'from': getcoinbase(), 'data': "0x2f54bf6e000000000000000000000000" + hex(int(addr, 16))[:2].strip('L').rjust(0x20, '0'), 'to':address}])
req = buildreq('eth_sendTransaction', [{'from': getcoinbase(), 'data': "0x2f54bf6e000000000000000000000000" + hex(int(getcoinbase(), 16))[:2].strip('L').rjust(0x20, '0'), 'to':address}])
req
getcoinbase
getcoinbase()
def isowner(addr):
    req = buildreq('eth_sendTransaction', [{'from': getcoinbase(), 'data': "0x2f54bf6e000000000000000000000000" + hex(int(addr, 16))[2:].strip('L').rjust(0x20, '0'), 'to':address}])
    return doreq(req).text 
isowner(getcoinbase())
getcoinbase()
isowner('0x0')
isowner('0x1')
getcoinbase()
isowner('0x544e3941ef92d6b2da1335afb8b203b1706bdeb9')
isowner(getcoinbase())
isowner(getcoinbase())
def tranresult(hash):
    req = buildreq('eth_getTransactionByHash', [hash])
    return doreq(req).text 
tranresult('0xf9c5fa94959e84af1403a781eef8706ca79f51e314aae64a8b980f090d324e5d')
def tranresult(hash):
    req = buildreq('eth_getTransactionReceipt', [hash])
    return doreq(req).text 
tranresult('0xf9c5fa94959e84af1403a781eef8706ca79f51e314aae64a8b980f090d324e5d')
tranresult('0xe66a4c7b25d51b48bcd3d7617c3ec969ac39af15cac4c2252d047f248a1e1f76')
tranresult('0x62e3fc8880994247def03bba42e966ef6bf75a2c879de46356fa8c3c48c4ad96')

    global bank
    req = {
        'jsonrpc': '2.0',
        'method': 'eth_accounts',
        'params': [],
        'id': 0
    }
    print json.loads(doreq(req).text)['result']

global bank
req = {
        'jsonrpc': '2.0',
        'method': 'eth_accounts',
        'params': [],
        'id': 0
    }
print json.loads(doreq(req).text)['result']

global bank
req = {
        'jsonrpc': '2.0',
        'method': 'eth_accounts',
        'params': [],
        'id': 0
    }
print json.loads(doreq(req).text)['result']
getcoinbase()
def isowner(addr):
    req = buildreq('eth_call', [{'from': getcoinbase(), 'data': "0x2f54bf6e000000000000000000000000" + hex(int(addr, 16))[2:].strip('L').rjust(0x20, '0'), 'to':address}])
    return doreq(req).text 
bank = 'f94d3692e732b23273e2413e3ee37a8d'
isowner(getcoinbase())
isowner('0x544e3941ef92d6b2da1335afb8b203b1706bdeb9')
isowner('0x544e3941ef92d6b2da')
isowner('0x544e3941ef92d6b2da1395afb8b203b1706bdeb9')
req = buildreq('eth_call', [{'from': getcoinbase(), 'data': "0x4b8fcc14000000000000000000000000" + hex(int(addr, 16))[2:].strip('L').rjust(0x20, '0'), 'to':address}])
print doreq(req).text 
addr = getcoinbase()
req = buildreq('eth_call', [{'from': getcoinbase(), 'data': "0x4b8fcc14000000000000000000000000" + hex(int(addr, 16))[2:].strip('L').rjust(0x20, '0'), 'to':address}])
print doreq(req).text 
address
'0x627a7a723058'.decode('hex')
'627a7a723058'.decode('hex')
