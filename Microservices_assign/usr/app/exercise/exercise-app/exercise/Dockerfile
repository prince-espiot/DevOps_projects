#########################
# Enter your code below #
#########################
# syntax=docker/dockerfile:1

FROM python:3.10.8-alpine3.16
WORKDIR /usr/app
ENV DEBIAN_FRONTEND=noninteractive
ENV FLASK_APP=app.py
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

