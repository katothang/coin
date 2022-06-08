FROM python:latest

WORKDIR /app

COPY src/* ./
RUN pip3 install -r requirements.txt

CMD [ "python3", "./main.py"]