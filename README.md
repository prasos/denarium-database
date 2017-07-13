<!-- -*- mode: markdown; coding: utf-8 -*- -->
# Official Denarium database

This is the official [Denarium Bitcoin](https://denarium.com)
database. The database is a single file, [coin.tsv](coin.tsv) which
contains current status of all Denarium Bitcoins ever produced in
tab-separated format.

Provided data was automatically produced at 2017-07-13 18:01:07 UTC.
Content is signed by bitcoin address
[1PrasosHejKfuRW6XgB6iYwftZQcatrMNC](https://www.blocktrail.com/BTC/address/1PrasosHejKfuRW6XgB6iYwftZQcatrMNC).
Proof of origin and existence of the data is in transaction
[232ea8b62427d64965ae6c4818c0851604424bf127f456cf88155e3b2b93f7de](https://www.blocktrail.com/BTC/tx/232ea8b62427d64965ae6c4818c0851604424bf127f456cf88155e3b2b93f7de).

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
F0113  | [Denarium 1 BTC Parity Gold Coin](https://denarium.com/product/denarium-1-btc-parity-gold-coin)
F0113X | [Denarium 1 BTC Parity Gold Coin (empty)](https://denarium.com/product/denarium-1-btc-parity-gold-coin)
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

### Production batch code

The format is in YYYY-MM-DD-N format and is composed of year, month,
day of the production set-up. The same set-up may have been used for
multiple days. In case of multiple set-ups per a day, N is
incremented.
