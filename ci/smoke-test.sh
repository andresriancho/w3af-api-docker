#!/usr/bin/env bash

git clone https://github.com/andresriancho/w3af-api-client.git
cd w3af-api-client
nosetests -v -s ci
