FROM python:3.8-slim

# prepare env
COPY requirements.txt /root/requirements.txt
RUN pip install -r requirements.txt

# prepare backend app
WORKDIR /backend
COPY views /backend/views
COPY main.py /backend/main.py
COPY config.json /backend/config.json

# expose port
EXPOSE 5000

ENTRYPOINT [ "/bin/bash" ]