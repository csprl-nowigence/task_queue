FROM python:3.8.8-buster

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100

RUN pip install -U pip wheel setuptools

# Copy only requirements to cache them in docker layer
WORKDIR /code
COPY requirements.txt /code/

# Project initialization:
RUN pip install -r requirements.txt

# Creating folders, and files for a project:
COPY *.py /code/
#COPY worker.py /code/worker.py
