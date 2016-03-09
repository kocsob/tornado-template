FROM alpine:latest

MAINTAINER Balazs Kocso

RUN apk add -U python
RUN apk add -U py-pip
RUN apk add -U nodejs
RUN apk add -U git
RUN npm install -g bower

ADD . /tornado_template
WORKDIR /tornado_template

RUN pip install -r requirements.txt
RUN bower install --allow-root

CMD [ "python", "__main__.py" ]

EXPOSE 8000
