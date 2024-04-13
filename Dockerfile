FROM python:latest

WORKDIR /app

COPY ./*.py /app/

CMD ["python", "assistant.py"]