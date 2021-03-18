FROM golang:1.15

EXPOSE 8080

WORKDIR /usr/src/app

COPY ./example-backend .

ENV REQUEST_ORIGIN="localhost:5000"

RUN go build

CMD ["./server"]