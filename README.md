<!-- -*- mode: markdown; coding: utf-8 -*- -->
# Official Denarium database

This is the official [Denarium Bitcoin](https://denarium.com)
database. This database dump consists of two files; `README.md`
(this file) and `coin.tsv` which contains current status of all
Denarium Bitcoins ever produced in tab-separated format.

Provided data was automatically produced at 2015-10-12 00:36:12 UTC.
Content is signed by bitcoin address
[1PrasosHejKfuRW6XgB6iYwftZQcatrMNC](https://www.blocktrail.com/BTC/address/1PrasosHejKfuRW6XgB6iYwftZQcatrMNC).
Proof of origin and existence of the data is in transaction
[6d5145f9492cfc5cc6335f695c836661aadbab533f4f4b7ed4e9fdf1885dba95](https://www.blocktrail.com/BTC/tx/6d5145f9492cfc5cc6335f695c836661aadbab533f4f4b7ed4e9fdf1885dba95).

To verify the origin, check that the transaction originates from our bitcoin
address. To verify existence, calculate SHA256 of `coins.tsv` and compare
it to last bytes of OP_RETURN output of given bitcoin transaction.
