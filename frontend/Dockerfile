FROM node:17-alpine
WORKDIR /app
COPY package*.json /app

RUN npm i --silent
# this is used for development puroses only, great for testing!
RUN npm i -g react-scripts@5.0.0 

COPY . ./

CMD [ "npm", "start" ]