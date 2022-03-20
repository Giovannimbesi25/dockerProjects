FROM ubuntu
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update 
RUN apt-get -y install python3 python3-pip
RUN apt-get -y install python3-tk
RUN  pip install plotext Pillow
WORKDIR /app
COPY . /app
CMD python3 app.py

