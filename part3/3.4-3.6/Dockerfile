FROM golang:alpine3.13

EXPOSE 8080

WORKDIR /usr/src/app

COPY ./example-backend .

ENV REQUEST_ORIGIN=http://localhost:5000

RUN apt-get update && apt-get install wget -y \
    && apt-get install build-essential -y \
    && wget https://dl.google.com/go/go1.16.5.linux-amd64.tar.gz \
    && rm -rf /usr/local/go && tar -C /usr/local -xzf go1.16.5.linux-amd64.tar.gz \
    && rm -rf go1.16.5.linux-amd64.tar.gz \
    && apt-get purge -y --auto-remove wget \
    && rm -rf /var/lib/apt/lists/* \
    && go build && go test ./... \
    && rm -rf /usr/local/go \
    && apt-get purge -y --auto-remove build-essential \
    && useradd -m appuser

CMD ["./server"]