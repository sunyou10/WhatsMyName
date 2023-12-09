FROM python:3.10.12
WORKDIR /WhatsMyNAME

RUN pip3 install requests
RUN pip3 install beautifulsoup4

COPY main.py .

CMD [ "python3", "main.py" ]
