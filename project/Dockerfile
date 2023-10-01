FROM python:3.10
ENV PYTHONUNBUFFERED 1
RUN mkdir /drf_api
WORKDIR /drf_api
COPY . /drf_api/
RUN pip install -r requirements.txt
