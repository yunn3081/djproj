FROM python:3.9.6
LABEL maintainer hannah
RUN mkdir /django_tutorial
WORKDIR /django_tutorial
COPY . /django_tutorial/
RUN pip install -r requirements.txt
RUN apt update && apt install tzdata -y
ENV TZ="Asia/Taipei"
EXPOSE 5000