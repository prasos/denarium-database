<!-- -*- mode: markdown; coding: utf-8 -*- -->
# Official Denarium database

This is the official [Denarium Bitcoin](https://denarium.com)
database. The database is a single file, [coin.tsv](coin.tsv) which
contains current status of all Denarium Bitcoins ever produced in
tab-separated format.

Provided data was automatically produced at 2016-01-10 19:00:49 UTC.
Content is signed by bitcoin address
[1PrasosHejKfuRW6XgB6iYwftZQcatrMNC](https://www.blocktrail.com/BTC/address/1PrasosHejKfuRW6XgB6iYwftZQcatrMNC).
Proof of origin and existence of the data is in transaction
[264b4151ccdbd9d681940a082c2ffd691f8715514c172618108c51926118ef9d](https://www.blocktrail.com/BTC/tx/264b4151ccdbd9d681940a082c2ffd691f8715514c172618108c51926118ef9d).

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
F0107  | Denarium 1/100
F0107X | Denarium 1/100 (empty)
F0108  | Denarium 1/10
F0108X | Denarium 1/10 (empty)

### Production batch code

The format is in YYYY-MM-DD-N format and is composed of year, month,
day of the production set-up. The same set-up may have been used for
multiple days. In case of multiple set-ups per a day, N is
incremented.
