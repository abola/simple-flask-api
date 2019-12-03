FROM python:3.7-slim

WORKDIR /opt/flask

COPY src/ /opt/flask/

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "api.py"]
