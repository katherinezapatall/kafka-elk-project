FROM python:3.10-bullseye
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /code
RUN apt update && apt-get install -y gcc
RUN apt-get update && apt install -y librdkafka-dev && \
    apt install -y python3-dev && \
    apt install -y libssl-dev 
WORKDIR /code
ADD . /code/
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["python", "-u", "log_producer.py"]