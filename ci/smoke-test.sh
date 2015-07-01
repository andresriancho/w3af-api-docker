#!/usr/bin/env bash

docker run -d \
           -v ~/.w3af:/root/.w3af \
           -v ~/w3af-shared:/root/w3af-shared \
           -p 5000:5000 \
           -p 9001:9001 \
           andresriancho/w3af-api

git clone https://github.com/andresriancho/w3af-api-client.git
cd w3af-api-client
nosetests -v -s ci
