FROM python:3.11

RUN apt-get update

RUN apt-get install sudo -y

ADD main.py .

RUN pip install requests

ENTRYPOINT ["python", "./main.py"]

