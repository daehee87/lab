FROM ubuntu:20.04

RUN sed -i "s/http:\/\/archive.ubuntu.com/http:\/\/kr.archive.ubuntu.com/g" /etc/apt/sources.list

# install related libraries
RUN apt update && apt-get install -y python3-dev python3-venv python3 build-essential python3-pip libffi-dev python3-setuptools libssl-dev

# setup configs
ADD web /web

# at root
WORKDIR /web

STOPSIGNAL SIGTERM
CMD ["/web/run.sh"]


