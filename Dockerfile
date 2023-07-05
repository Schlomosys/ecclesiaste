FROM python:3.9-slim-buster

COPY ecclesiaste/config.py /ecclesiaste/
COPY ecclesiaste/bot.py /ecclesiaste/
COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

WORKDIR /ecclesiaste
CMD ["python3", "bot.py"]