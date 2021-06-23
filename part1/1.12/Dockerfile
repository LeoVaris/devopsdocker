FROM node

EXPOSE 5000

WORKDIR /usr/src/app

COPY ./example-frontend .

RUN npm install
RUN npm run build
RUN npm -y install -g serve
RUN useradd -m appuser

USER appuser

CMD ["serve", "-s", "-l", "5000", "build"]

