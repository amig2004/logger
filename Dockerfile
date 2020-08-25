FROM python:3.8-slim

# prepare env
COPY requirements.txt /root/requirements.txt
RUN pip install -r /root/requirements.txt

# prepare backend app files
WORKDIR /backend
COPY __init__.py /backend/__init__.py
COPY database.py /backend/database.py
COPY utils.py /backend/utils.py

# copy views files
COPY tags.py /backend/tags.py
COPY logs.py /backend/logs.py
COPY persons.py /backend/persons.py

#configuration file
COPY config.json /backend/config.json

#prepare environment vars
ENV FLASK_APP=src
ENV FLASK_ENV=development

WORKDIR /

# comment CMD and uncomment entry point if want to use container as interactive
CMD flask run

#ENTRYPOINT [ "/bin/bash" ]