<!-- -*- mode: markdown; coding: utf-8 -*- -->
# Official Denarium database

This is the official [Denarium Bitcoin](https://denarium.com)
database. The database is a single file, [coin.tsv](coin.tsv) which
contains current status of all Denarium Bitcoins ever produced in
tab-separated format.

If you want to see coin details and transactions in a visual format, we also have the [Denarium Database Explorer](https://denarium.com/database).

Provided data was automatically produced at 2019-08-02 15:14:52 UTC.
Content is signed by bitcoin address
[1PrasosHejKfuRW6XgB6iYwftZQcatrMNC](https://www.blocktrail.com/BTC/address/1PrasosHejKfuRW6XgB6iYwftZQcatrMNC).
Proof of origin and existence of the data is in transaction
[11a37d399716a61f09426a066f3bec0c81a6dfd2c8fa1e3602248853505c7a88](https://www.blocktrail.com/BTC/tx/11a37d399716a61f09426a066f3bec0c81a6dfd2c8fa1e3602248853505c7a88).

## Verification

To verify the origin, check that the transaction originates from our bitcoin
address. To verify existence, calculate SHA256 of [coin.tsv](coin.tsv) and
compare it to last bytes of OP_RETURN output of given bitcoin transaction.

There is also [verify.py](verify.py) which does all of this
automatically. See that file for instructions.

## Format

Data is separated to columns using tab (`\t`) character. Character set
is ASCII. It can be easily imported to common databases and
spreadsheet editors.

Column       | Description
------------ | -----------
address      | Bitcoin address of the coin
serial       | Serial number (L series are pre-loaded coins)
pubkey       | Reserved for future use
sku          | Stock keeping unit (see below)
denomination | Bitcoin value of that coin after activation
batch        | Production batch code (see below)
created\_at  | Timestamp of coin creation (importing is done in batches so this is not the exact moment of manufacture)
status       | Coin status (see below)
pubkey\_2fa  | Reserved for future use
txid         | Funding transaction ID. (Some of the txid's have been subject to malleability attacks)

### Coin status

Status            | Description
----------------- | -----------
new               | Successfully manufactured, not shipped yet
failed            | Destroyed on the production line
sample            | Random samples for quality control
shipped           | Shipped but not yet activated
reported\_missing | Reported as missing by customer
reported\_damaged | Reported as damaged by customer
reported\_ok      | Reported as OK by customer
missing           | Confirmed as missing
complete          | Successfully activated

### SKU

SKU   | Release Year| Description
----- | ------------| --------------
F0107 | 2015        | [Denarium 1/100](https://status.denarium.com/coin/#/F0107)
F0108 | 2015        | [Denarium 1/10](https://status.denarium.com/coin/#/F0108)
F0109 | 2016        | [Denarium 1 BTC Silver](https://status.denarium.com/coin/#/F0109)
F0110 | 2016        | [Denarium 1 BTC Silver Patinated](https://status.denarium.com/coin/#/F0110)
F0111 | 2016        | [Denarium 1 BTC Silver Golden Edition](https://status.denarium.com/coin/#/F0111)
F0112 | 2018        | [Denarium Custom Silver](https://status.denarium.com/coin/#/F0112)
F0113 | 2017        | [Denarium 1 BTC Parity Gold Coin](https://status.denarium.com/coin/#/F0113)
F0114 | 2018        | [Denarium 1/2 BTC Gold](https://status.denarium.com/coin/#/F0114)
F0115 | 2018        | [Denarium 1 BTC Patinated Bronze](https://status.denarium.com/coin/#/F0115)
F0116 | 2018        | [Denarium 1/2 BTC Gold 2018](https://status.denarium.com/coin/#/F0116)
F0117 | 2015        | [Denarium 1/100 BTC Gold Plated](https://status.denarium.com/coin/#/F0117)
F0118 | 2015        | [Denarium 1/10 BTC Gold Plated](https://status.denarium.com/coin/#/F0118)
F0119 | 2015        | [Denarium Custom](https://status.denarium.com/coin/#/F0119)
F0120 | 2016        | [Denarium Custom 0,01 - 5 BTC Gold Plated](https://status.denarium.com/coin/#/F0120)
F0121 | 2016        | [Denarium 1/100 Prototype #1](https://status.denarium.com/coin/#/F0121)
F0122 | 2016        | [Denarium 1/10 Prototype #2](https://status.denarium.com/coin/#/F0122)
F0123 | 2016        | [Denarium 1/100 Prototype #3](https://status.denarium.com/coin/#/F0123)
F0124 | 2018        | [Denarium 1 BTC Parity Gold Coin Mock-up](https://status.denarium.com/coin/#/F0124)
F0125 | 2018        | [Denarium 1 BTC Silver Mock-up (Patinated Lead)](https://status.denarium.com/coin/#/F0125)
F0126 | 2018        | [Denarium 1 BTC Silver Mock-up (Patinated Bronze)](https://status.denarium.com/coin/#/F0126)
F0127 | 2019        | [Denarium 1 BTC Bi-metallic coin prototype](https://status.denarium.com/coin/#/F0127)
F0128 | 2019        | [Denarium 1 BTC Parity coin Copper mock-up ](https://status.denarium.com/coin/#/F0128)
F0129 | 2018        | [Denarium Gold Bar 2018](https://status.denarium.com/coin/#/F0129)
F0130 | 2018        | [Denarium Custom Gold Plated 2018](https://status.denarium.com/coin/#/F0130)
F0131 | 2019        | [Denarium 1/10 BTC 2015 Error coins](https://status.denarium.com/coin/#/F0131)
F0132 | 2019        | [Denarium 2015 Custom Error coin](https://status.denarium.com/coin/#/F0132)
F0133 | 2019        | [Denarium 1 BTC Patinated Bronze Mockup coin](https://status.denarium.com/coin/#/F0133)
F0140 | 2019        | [Denarium Custom Silver Antiqued Golden Edition coin](https://status.denarium.com/coin/#/F0140)
F0141 | 2019        | [Denarium Custom Silver Antiqued Edition coin](https://status.denarium.com/coin/#/F0141)
F0142 | 2019        | [Denarium Custom Gold Plated 2019 Special Edition](https://status.denarium.com/coin/#/F0142)
F0143 | 2019        | [Denarium Custom Gold Plated 2019](https://status.denarium.com/coin/#/F0143)



The X in the SKU means that the coin is sold as empty and in most cases, the serial number begins with an E. For mock-up coins, prototypes and new models we use Bitcointalk for auctioning these pieces. These coins serial number usually starts with an A.

### Serial number

SERIAL | Description
------ | -----------
A      | Auction coin (unique pieces sold as Bitcointalk)
E      | Sold as empty or multisig
L      | Sold as loaded with bitcoins
M      | Used for special multisig coins


### SKU JSON

The file coin_sku.json contains all the products with their corresponding SKU names. It is useful for creating charts and other tools to the top of the Denarium Database.

### Production batch code

The format is in YYYY-MM-DD-N format and is composed of year, month,
day of the production set-up. The same set-up may have been used for
multiple days. In case of multiple set-ups per a day, N is
incremented.
