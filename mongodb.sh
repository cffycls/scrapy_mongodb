#!/bin/bash

docker rm -f mongo && docker run --name mongo -p=27017:27017 -d mongo
