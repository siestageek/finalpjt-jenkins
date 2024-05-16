FROM node:18-alpine

WORKDIR /app


# package.json, package-lock.json 복사
# package.json : npm install
# packge-lock.json : npm ci --only=production (추천)
COPY package*.json .

RUN npm install  --save 
# RUN npm ci --only=production

COPY . .

EXPOSE 3000

CMD ["npm", "start"]
