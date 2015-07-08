#!/usr/bin/env bash

set -x
set -e

# Start the docker container that we just built
docker run -d \
           -v ~/.w3af:/root/.w3af \
           -v ~/w3af-shared:/root/w3af-shared \
           -p 5000:5000 \
           -p 9001:9001 \
           andresriancho/w3af-api:latest

# Wait for the container to start
sleep 20

# Run the tests
git clone https://github.com/andresriancho/w3af-api-client.git
cd w3af-api-client
git rev-parse --short HEAD
nosetests -v -s ci
