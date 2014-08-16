dskvs
=====

Deadly Simple KVS without a lot of features, but with atomic text file loader.

This project is my personal experimental project, so please do not use it in production or anywhere!!


What dskvs can't do
-------------------


- dskvs can't update value by specifying key
- dskvs can't load balance requests
- dskvs can't have cluster
- dskvs can't understand SQL-ish DSL
- dskvs can't read and return structured data


What dskvs can do
-----------------

- dskvs can receive a HTTP request and return a list of values in JSON format
- dskvs can atomically load data from good-old TSV

.. this is it.


Install(Python)
---------------

Clone and pip install.
```
git clone git@github.com:achiku/dskvs.git
cd dskvs
pip install -r requirements/development.txt
```


Create test data.
```
mkdir data
cp ./tests/testdata.tsv ./data
```


Run debug-enabled server.
```
python dskvs/dskvs.py
```

Access to the followin URL.

- [http://localhost:5001/test/user_a](http://localhost:5001/test/user_a)
- [http://localhost:5001/test/user_b](http://localhost:5001/test/user_b)

You'll get some JSON list, and that is it.



Install(Golang)
---------------

todo: write setup for golang
