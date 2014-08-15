dskvs
=====

Deadly Simple KVS without a lot of features, but with atomic text file loader.
It acts like usual KVS with RESTful interface but lacks a lot of features.


What dskvs can't do
===================

- dskvs can't update value by specifying key
- dskvs can't load balance requests
- dskvs can't have cluster
- dskvs can't understand SQL-ish DSL
- dskvs can't read and return structured data


What dskvs can do
=================

- dskvs can receive HTTP request and return list of values in JSON format
- dskvs can atomically load data from good-old TSV

.. this is it.
