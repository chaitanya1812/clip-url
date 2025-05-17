#! /bin/bash

docker build -t clip-url .   


docker run -p 10000:10000 clip-url