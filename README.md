# GlobalGiving Hackathon Project

GlobalGiving: [globalgiving.org](https://www.globalgiving.org/)

Goal: Implement method for field agents to provide project updates via cellular networks.

## Pre-requisites

* S3 bucket for the reports, put in the `report_bucket` field in `serverless.env.yml`.
* DynamoDB table, put in the `ddb` field in `serverless.env.yml`.
* Twilio accounts for the registration endpoint and the update endpoint, put values in
the appropriate auth token and sid fields.

## Deployment

Requires the [serverless](https://serverless.com) tool.

Using the Dockerfile contained in this project to generate a base docker container:

```
$ docker run --name hackathon -itd -v "${HOME}/reinvent-hackathon-2017":/root image/name:latest
$ docker exec -it hackathon /bin/sh
$ cd ~
$ npm install -g serverless
$ serverless plugin install -n serverless-python-requirements
$ serverless plugin install -n serverless-parameters
$ serverless deploy
```


