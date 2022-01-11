#!#/bin/env bash

set -x
set -e

version=$(curl -H 'Content-type: application/json' https://git.door43.org/api/v1/version | jq -r '.version' | tr '+' '-')

curl -H 'Content-type: application/json' -X POST -d "{\"options\": {\"packageName\": \"dcs_api_client\", \"projectName\": \"dcs-api-client\", \"packageVersion\": \"$version\", \"packageUrl\": \"https://github.com/unfoldingWord-dev/python-dcs-client\"}, \"swaggerUrl\": \"https://git.door43.org/swagger.v1.json\"}" https://generator.swagger.io/api/gen/clients/python | curl $(jq -r '.link') -o dcs_api_client.zip
unzip dcs_api_client.zip
rsync -P -rvzc --delete --exclude=update_client.sh --exclude=python-client --exclude=.git* python-client/ ./
rm -rf python-client

