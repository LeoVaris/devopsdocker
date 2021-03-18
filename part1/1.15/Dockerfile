FROM ubuntu:20.04

WORKDIR /usr/src/app

COPY ./Regex-trainer .

RUN apt-get update -y \ 
    && apt-get install -y python3 \ 
    && apt-get install -y python3-venv \
    && apt-get install -y python3-pip
RUN pip3 install -r requirements.txt

EXPOSE 5000

ENTRYPOINT [ "flask" ]
CMD [ "run" ]