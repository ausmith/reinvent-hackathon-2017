FROM alpine

RUN apk update && apk add unzip curl python3 openntpd
RUN apk add --update nodejs nodejs-npm zip
