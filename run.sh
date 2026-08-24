#!/bin/bash
ID="$(basename $PWD)"
EXISTING_CONTAINER=$(docker ps -a -f name=web-$ID_site -q)

if [ "$EXISTING_CONTAINER" != "" ]; then
  sudo docker rm web-$ID_site
fi

sudo docker run --security-opt \
                seccomp=unconfined \
                -v $PWD/web:/web \
                -p 4000:4000/tcp \
                --name "web-$ID-nick" \
                -it \
		"web-${ID}_site"
