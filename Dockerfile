FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN \
  apt-get update \
  && apt-get -y install libpq-dev gcc \
  && pip3 install --no-cache-dir -r /app/requirements.txt

COPY . /app/

CMD [ "uvicorn", "main:app", "--host=0.0.0.0", "--reload" ]
