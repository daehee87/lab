#!/bin/bash
ID="$(basename $PWD)"
EXISTING_CONTAINER=$(docker ps -a -f name=web-$ID-nick -q)

if [ "$EXISTING_CONTAINER" != "" ]; then
  sudo docker rm web-$ID-nick
fi

sudo docker run --security-opt \
                seccomp=unconfined \
                -v $PWD/web:/web \
                -p 4000:4000/tcp \
                --name "web-$ID-nick" \
                -it \
                "web-$ID"
