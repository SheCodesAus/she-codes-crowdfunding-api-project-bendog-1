ARG PYTHON_VERSION=3.10-slim-buster

FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /code

WORKDIR /code

COPY requirements.txt /tmp/requirements.txt

RUN set -ex && \
    pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /root/.cache/

COPY crowdfunding/ /code/

RUN python manage.py collectstatic --noinput
RUN chmod +x /code/run.sh

EXPOSE 8000

# replace demo.wsgi with <project_name>.wsgi
CMD ["/code/run.sh"]