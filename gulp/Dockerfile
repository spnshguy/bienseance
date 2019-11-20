FROM node:boron-alpine

ADD package.json /bienseance/gulp/package.json
WORKDIR /bienseance/gulp/

RUN npm install -g gulp-cli && npm install webpack@3 && npm install
