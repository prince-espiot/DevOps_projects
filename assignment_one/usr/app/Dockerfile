# syntax=docker/dockerfile:1
FROM alpine:3.12
WORKDIR /usr/app
ENV VAR "10"
ENV MSG "Hello Docker!"
COPY fibonacci.sh ./
COPY helloDocker.sh ./
RUN chmod +x fibonacci.sh
RUN chmod +x helloDocker.sh
RUN ./fibonacci.sh
RUN ./helloDocker.sh




