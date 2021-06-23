FROM python:3.7

WORKDIR /usr/app

COPY ./run.py ./run.py

RUN pip3 install GitPython

ENTRYPOINT [ "python3", "run.py" ]