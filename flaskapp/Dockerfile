# pulling the base image
FROM python:3.7.0-alpine3.8

# Creating a folder and moving into it
WORKDIR /usr/src/app

# Copying the dependency list 
COPY requirements.txt ./

# Installing the python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copying the flask code into the container
COPY . .

ENV FLASK_APP=app.py

EXPOSE 5000

# Starting the server
CMD flask run --host=0.0.0.0

