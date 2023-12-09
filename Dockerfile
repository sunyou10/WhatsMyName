FROM python:3.8-buster
WORKDIR /WhatsMyNAME

RUN pip3 apt-get update && apt-get install -y
RUN pip3 install requests
RUN pip3 install beautifulsoup4

COPY main.py .

CMD [ "python3", "main.py" ]
