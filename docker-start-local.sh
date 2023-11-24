#!/bin/bash 

MICROSERVICE="api_url_adm"

docker network create urlshortener
docker rm $MICROSERVICE --force
docker build --tag $MICROSERVICE:latest .
docker image prune -f
docker run -t -d --name $MICROSERVICE --publish 8081:80 --network urlshortener $MICROSERVICE:latest
