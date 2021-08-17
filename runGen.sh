#!/bin/bash

docker run --rm -it \
			-w /gen \
			-e GEN_DIR=/gen \
			-u "$(id -u):$(id -g)" \
			-v "${PWD}:/gen" \
			swaggerapi/swagger-codegen-cli generate \
			-i https://git.imada.sdu.dk/swagger.v1.json \
			-l python \
			-DpackageName=giteapy \
			-DpackageVersion=1.15.0-rc3 \
			-DpackageUrl=https://github.com/jakobandersen/giteapy \
			--api-package api \
			--git-repo-id giteapy \
			--git-user-id jakobandersen
find giteapy -type f -iname "*.py" | xargs sed -i "s/^from api/from .api/"
find giteapy/api -type f -iname "*.py" | xargs sed -i "s/^from \.api/from /"
