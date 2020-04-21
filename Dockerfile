FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
RUN apt-get -y update && apt-get -y install ffmpeg exiftool
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
