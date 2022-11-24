FROM python:3.9-slim

ENV PROJECT_ROOT /project
ENV SRC_DIR /doc_bot
ENV DEPLOY_DIR ./deploy

RUN mkdir $PROJECT_ROOT
COPY $SRC_DIR/gunicorn.conf.py $PROJECT_ROOT
COPY $DEPLOY_DIR/run_django.sh $PROJECT_ROOT

RUN apt-get update && \
    apt-get install -y postgresql-client-common postgresql-client libpq-dev && \
    apt-get install -y build-essential curl && \
    curl -sL https://deb.nodesource.com/setup_14.x | bash - && \
    apt-get install -y nodejs --no-install-recommends && \
    rm -rf /var/lib/apt/lists/* /usr/share/doc /usr/share/man && \
    apt-get clean

RUN pip install --upgrade pip wheel pipenv

COPY ./Pipfile $PROJECT_ROOT
COPY ./Pipfile.lock $PROJECT_ROOT

WORKDIR $PROJECT_ROOT
RUN pipenv install --deploy --system --dev

COPY ./$SRC_DIR $PROJECT_ROOT

RUN chmod +x $PROJECT_ROOT/run_django.sh
CMD ["./run_django.sh"]