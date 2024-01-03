# simpris docker file
# 2020-04-25

# pull python base image
FROM python:3

# so docker does not screw up console output
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN mkdir /code
WORKDIR /code

# Upgrade pip
RUN pip install pip -U
COPY docker-requirements.txt /code/
RUN pip install -r docker-requirements.txt
COPY . /code/
