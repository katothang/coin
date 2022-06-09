FROM python:latest

WORKDIR /app

COPY src src

CMD ["python3", "src/main.py", "&"]