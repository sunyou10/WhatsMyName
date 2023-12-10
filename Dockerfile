FROM python:3.8-buster
WORKDIR /WhatsMyName
COPY main.py .

RUN apt-get update && apt-get install tor -y
RUN pip3 install requests BeautifulSoup4 pyfiglet clint PySocks urllib3

CMD ["python3", "main.py"]
