FROM python:3.5
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y binutils \
  libproj-dev \
  gdal-bin

# Requirements have to be pulled and installed here, otherwise caching won't work
COPY ./requirements /requirements
RUN pip install -r /requirements/local.txt
RUN pip install -r /requirements/test.txt

COPY ./compose/django/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

WORKDIR /app

ENTRYPOINT ["/entrypoint.sh"]
