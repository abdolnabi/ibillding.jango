FROM python:3

RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    gettext \
    curl

RUN mkdir /app

# Requirements are installed here to ensure they will be cached.
COPY ./requirements.txt /requirements.txt
RUN pip install /requirements.txt

COPY . /app

WORKDIR /app

CMD ["gunicron" , "bcm.wsgi:application", "--chdir bcm", "--bind 127.0.0.1:8000", "--workers=1"]
