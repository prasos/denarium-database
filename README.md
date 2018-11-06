<!-- -*- mode: markdown; coding: utf-8 -*- -->
# Official Denarium database

This is the official [Denarium Bitcoin](https://denarium.com)
database. The database is a single file, [coin.tsv](coin.tsv) which
contains current status of all Denarium Bitcoins ever produced in
tab-separated format.

Provided data was automatically produced at 2018-11-06 00:56:00 UTC.
Content is signed by bitcoin address
[1PrasosHejKfuRW6XgB6iYwftZQcatrMNC](https://www.blocktrail.com/BTC/address/1PrasosHejKfuRW6XgB6iYwftZQcatrMNC).
Proof of origin and existence of the data is in transaction
[72ad85500528b006e5f76d834624d69374e5e639d18e04d9b2346249927ea67a](https://www.blocktrail.com/BTC/tx/72ad85500528b006e5f76d834624d69374e5e639d18e04d9b2346249927ea67a).

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

SKU    | Description
------ | -----------
F0107  | [Denarium 1/100](https://denarium.com/product/denarium-10-000-bits)
F0107X | [Denarium 1/100 (empty)](https://denarium.com/product/denarium-10-000-bits-empty)
F0108  | [Denarium 1/10](https://denarium.com/product/denarium-100-000-bits)
F0108X | [Denarium 1/10 (empty)](https://denarium.com/product/denarium-100-000-bits-empty)
F0109  | [Denarium 1 BTC Silver](https://denarium.com/product/denarium-1-btc)
F0109X | [Denarium 1 BTC Silver (empty)](https://denarium.com/product/denarium-1-btc-empty)
F0110  | [Denarium 1 BTC Silver Patinated](https://denarium.com/product/denarium-1-btc-patinated)
F0110X | [Denarium 1 BTC Silver Patinated (empty)](https://denarium.com/product/denarium-1-btc-patinated)
F0111  | [Denarium 1 BTC Silver Golden Edition](https://denarium.com/product/denarium-1-btc-golden-edition)
F0111X | [Denarium 1 BTC Silver Golden Edition (empty)](https://denarium.com/product/denarium-1-btc-golden-edition)
F0112  | [Denarium Custom Silver](https://denarium.com/product/denarium-custom-silver)
F0112X | [Denarium Custom Silver (empty)](https://denarium.com/product/denarium-custom-silver)
F0113  | [Denarium 1 BTC Parity Gold Coin](https://denarium.com/product/denarium-1-btc-parity-gold-coin)
F0113X | [Denarium 1 BTC Parity Gold Coin (empty)](https://denarium.com/product/denarium-1-btc-parity-gold-coin)
F0114  | [Denarium 1/2 BTC Gold](https://denarium.com/product/denarium-1-2-btc-gold)
F0114X | [Denarium 1/2 BTC Gold (empty)](https://denarium.com/product/denarium-1-2-btc-gold)
F0115  | [Denarium 1 BTC Patinated Bronze](https://denarium.com/product/denarium-1-btc-bronze-patinated)
F0115X | [Denarium 1 BTC Patinated Bronze (empty)](https://denarium.com/product/denarium-1-btc-bronze-patinated)
F0116  | [Denarium 1/2 BTC Gold 2018](https://denarium.com/product/denarium-1-2-btc-gold-2018)
F0116X | [Denarium 1/2 BTC Gold 2018 (empty)](https://denarium.com/product/denarium-1-2-btc-gold-2018)
F0117  | [Denarium 1/100 BTC Gold Plated](https://denarium.com/product/denarium-1100-btc-gold-plated)
F0117X | [Denarium 1/100 BTC Gold Plated (empty)](https://denarium.com/product/denarium-1100-btc-gold-plated)
F0118  | [Denarium 1/10 BTC Gold Plated](https://denarium.com/product/denarium-110-btc-gold-plated)
F0118X | [Denarium 1/10 BTC Gold Plated (empty)](https://denarium.com/product/denarium-110-btc-gold-plated)
F0119  | [Denarium Custom](https://denarium.com/product/denarium-with-custom-amount)
F0119X | [Denarium Custom (empty)](https://denarium.com/product/denarium-coin-empty)
F0120  | [Denarium Custom 0,01 - 5 BTC Gold Plated](https://denarium.com/product/denarium-custom-001-5-btc-gold-plated)
F0120X | [Denarium Custom 0,01 - 5 BTC Gold Plated (empty)](https://denarium.com/product/denarium-custom-001-5-btc-gold-plated)
F0121  | Denarium 1/100 Prototype #1
F0122  | Denarium 1/10 Prototype #2
F0123  | Denarium 1/100 Prototype #3
F0121X | Denarium 1/100 Prototype #1 (empty)
F0122X | Denarium 1/10 Prototype #2 (empty)
F0123X | Denarium 1/100 Prototype #3 (empty)
F0124X | [Denarium 1 BTC Parity Gold Coin Mock-up](https://status.denarium.com/coin/#/F0124)
F0125X | [Denarium 1 BTC Silver Mock-up (Patinated Lead)](https://status.denarium.com/coin/#/F0125)
F0126X | [Denarium 1 BTC Silver Mock-up (Patinated Bronze)](https://status.denarium.com/coin/#/F0126)
F0130  | [Denarium Custom Gold Plated 2018](https://denarium.com/product/denarium-custom-gold-plated-2018)
F0130X | [Denarium Custom Gold Plated 2018 (empty)](https://denarium.com/product/denarium-custom-gold-plated-2018)

### SKU JSON

The file coin_sku.json contains all the products with their corresponding SKU names. It is useful for creating charts and other tools to the top of the Denarium Database.

### Production batch code

The format is in YYYY-MM-DD-N format and is composed of year, month,
day of the production set-up. The same set-up may have been used for
multiple days. In case of multiple set-ups per a day, N is
incremented.
