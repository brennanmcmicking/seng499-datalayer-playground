FROM python:3.12-slim

WORKDIR /app

RUN apt-get update
RUN apt-get -y install libpq-dev gcc

COPY app/requirements.txt ./
RUN python3 -m venv env
ENV PATH=/app/env/bin:$PATH

RUN pip install -r requirements.txt

COPY ./app ./
COPY schema.sql ./

CMD ["python3", "-u", "wsgi.py"]