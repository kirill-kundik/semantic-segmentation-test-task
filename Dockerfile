FROM python:3.7.3

ADD . /app
WORKDIR /app

RUN pip install -r requirements.txt

ARG APP_PORT
EXPOSE $APP_PORT

CMD gunicorn -w 4 -b 127.0.0.1:$APP_PORT --access-logfile - --error-logfile - --log-level info --limit-request-line 0 "main:web_app"
