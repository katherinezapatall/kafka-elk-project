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
CMD ["python", "-u", "log_consumer.py"]




# FROM python:3.8

# WORKDIR /app
# COPY . /app

# RUN apt-get update && \
#   apt-get install -y --no-install-recommends gcc git libssl-dev g++ make && \
#   cd /tmp && git clone https://github.com/edenhill/librdkafka.git && \
#   cd librdkafka && git checkout tags/v1.9.0 && \
#   ./configure && make && make install && \
#   cd ../ && rm -rf librdkafka

# RUN pip install confluent-kafka==1.9.2

# CMD ["python", "log_consumer.py"]