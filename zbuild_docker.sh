#! /bin/bash

docker rm -f $(docker ps -a -q --filter "ancestor=clip-url")

docker build -t clip-url .   


docker run -p 8300:8500 clip-url