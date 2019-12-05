FROM python:3.7-slim

WORKDIR /opt/flask

COPY . /opt/flask

RUN pip install -r requirements.txt && \
    touch /alive

ENTRYPOINT ["python", "src/api.py"]
