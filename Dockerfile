# Image
FROM python:3.6-stretch

# Add files
COPY . /api

# Go to working directory
WORKDIR /api

# Install requirements
RUN pip3 install -r requirements.txt 