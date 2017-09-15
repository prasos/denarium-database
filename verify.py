#!/usr/bin/env python
#
# Simple validator for Denarium coin database contents using Insight
# API. Installation and usage instructions:
#
# 1) Copy this file outside git repository
# 2) Audit this file,
# 3) Set the following parameters to match your needs
# 4) Run me after every `git pull`

# Insight API URL. You must trust this party. Default: Bitpay
api = 'https://insight.bitpay.com/api'
# Directory where to find git repository. Default: current directory
mydir = ''
# Bitcoin address of Denarium Bitcoin bot
ours = '1PrasosHejKfuRW6XgB6iYwftZQcatrMNC'

### End of configurable options ###

from datetime import datetime
import hashlib
import os
import re
import requests

docproof_boiler = '6a28444f4350524f4f46' # OP_RETURN + length + "DOCPROOF"

# Obtain txid from README.md
with open(os.path.join(mydir,'README.md'), 'rb') as f:
    txid = re.search('[0-9a-f]{64}',f.read()).group()

# Calculate file hash
with open(os.path.join(mydir,'coin.tsv'), 'rb') as f:
    hash_on_file = hashlib.sha256(f.read()).hexdigest()

# Obtain transaction information
tx = requests.get(api+'/tx/'+txid).json()

# Extract and compare
origin = tx['vin'][0]['addr']

if tx['blockheight'] > -1:
  block_hash = tx['blockhash']
  time = datetime.fromtimestamp(tx['blocktime'])
else:
  block_hash = 'unconfirmed'
  time = 'unconfirmed'
confs = tx['confirmations']
script = tx['vout'][0]['scriptPubKey']['hex']
hash_on_chain = script[len(docproof_boiler):] 
matches = script.startswith(docproof_boiler) and hash_on_file == hash_on_chain

# Pretty-print
print('Transaction hash:  '+txid)
print('Block hash:        '+block_hash)
print('Payload hash:      '+hash_on_chain+' <- '+("OK" if matches else "FAIL"))
print('Payload origin:    '+origin+' <- '+("OK" if origin == ours else "FAIL"))
print('Payload timestamp: '+str(time)+' ('+str(confs)+' confirmations)')

# Use exit code to signal if it was OK
exit(0 if matches and origin==ours else 1)
