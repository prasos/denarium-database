<!-- -*- mode: markdown; coding: utf-8 -*- -->
# Official Denarium database

This is the official [Denarium Bitcoin](https://denarium.com)
database. This database dump consists of two files; [README.md](README.md)
(this file) and [coin.tsv](coin.tsv) which contains current status of all
Denarium Bitcoins ever produced in tab-separated format.

Provided data was automatically produced at 2015-10-12 13:37:03 UTC.
Content is signed by bitcoin address
[1PrasosHejKfuRW6XgB6iYwftZQcatrMNC](https://www.blocktrail.com/BTC/address/1PrasosHejKfuRW6XgB6iYwftZQcatrMNC).
Proof of origin and existence of the data is in transaction
[90b424d3766cc836a10a13796bf743f6496abda53b5e1efd7ff6929cb96bc2a0](https://www.blocktrail.com/BTC/tx/90b424d3766cc836a10a13796bf743f6496abda53b5e1efd7ff6929cb96bc2a0).

To verify the origin, check that the transaction originates from our bitcoin
address. To verify existence, calculate SHA256 of [coin.tsv](coin.tsv) and
compare it to last bytes of OP_RETURN output of given bitcoin transaction.
