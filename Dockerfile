FROM python:3.8-slim

RUN apt-get clean \
    && apt-get -y update

RUN apt-get -y install nginx \
    && apt-get -y install python3-dev \
    && apt-get -y install build-essential

WORKDIR /app
COPY . .

RUN pip install uwsgi
RUN pip install --no-cache-dir -r ./requirements.txt --src /usr/local/src

COPY nginx.conf /etc/nginx
RUN chmod +x ./start.sh
CMD ["./start.sh"]
