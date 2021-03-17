FROM ubuntu:18.04

WORKDIR /usr/src/app

COPY local.sh .

RUN apt-get update && apt-get -y install curl

CMD ./local.sh