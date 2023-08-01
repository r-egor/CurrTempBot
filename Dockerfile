FROM python:3.9-alpine

WORKDIR /app

ENV PYTHONPATH $PYTHONPATH:/app

RUN apk update && \
    apk add --no-cache supervisor

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

COPY . .

CMD ["supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]