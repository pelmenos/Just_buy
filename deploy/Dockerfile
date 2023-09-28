FROM python:3.10
ENV PYTHONUNBUFFERED 1
RUN git clone https://github.com/pelmenos/Just_buy.git /drf_src
WORKDIR /drf_src
CD /project
RUN pip install -r requirements.txt
VOLUME /drf_src
EXPOSE 8080
CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000
