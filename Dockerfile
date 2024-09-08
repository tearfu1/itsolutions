FROM python:3.12

WORKDIR /app

COPY . .
RUN pip install -U pip
RUN pip install moviepy

RUN apt-get update \
    && apt-get install -qq -y build-essential xvfb xdg-utils wget unzip ffmpeg libpq-dev vim libmagick++-dev fonts-liberation sox bc gsfonts --no-install-recommends\
    && apt-get clean

## ImageMagicK Installation
RUN apt install imagemagick

RUN cd itsolutions \
    && python manage.py runserver
