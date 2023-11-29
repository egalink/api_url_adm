#!/bin/bash 

IPV4_FROM="mongodb"
NETW_NAME="urlshortener" # replace this with your network name

docker pull mongo:jammy
docker network create $NETW_NAME
docker run -d --network $NETW_NAME \
	-e MONGO_INITDB_ROOT_USERNAME=urlshortener \
	-e MONGO_INITDB_ROOT_PASSWORD=supersecrets \
    --name $IPV4_FROM mongo:jammy

# IPV4_ADDRESS=$(docker network inspect "$NETW_NAME" | jq -r '.[] | .Containers | to_entries[] | .value.IPv4Address | split("/")[0]')
IPV4_ADDRESS=$(docker network inspect "$NETW_NAME" | jq -r '.[] | .Containers | to_entries[] | select(.value.Name == "'$IPV4_FROM'") | .value.IPv4Address | split("/")[0]')

if [ -z "$IPV4_ADDRESS" ]; then
    echo "No IPv4 addresses found."
    echo "Using defined MONGODB_HOST value in the .env file."
else
    echo "IPv4 address for the '$IPV4_FROM' container in the docker network called '$NETW_NAME' is: $IPV4_ADDRESS"
    echo "MONGODB_HOST=$IPV4_ADDRESS" >> .env 
fi

MICROSERVICE="api_url_adm"

docker rm $MICROSERVICE --force
docker build --tag $MICROSERVICE:latest .
docker image prune -f
docker run -t -d --name $MICROSERVICE --publish 8081:80 --network urlshortener $MICROSERVICE:latest

