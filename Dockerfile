FROM python:3.8-slim

# prepare env
COPY requirements.txt /root/requirements.txt
RUN pip install -r /root/requirements.txt

# prepare src app files
WORKDIR /src
COPY __init__.py /src/__init__.py
COPY database.py /src/database.py
COPY utils.py /src/utils.py

# copy views files
COPY tags.py /src/tags.py
COPY logs.py /src/logs.py
COPY logs_id.py /src/logs_id.py
COPY persons.py /src/persons.py

#configuration file
COPY config.json /src/config.json

#prepare environment vars
ENV FLASK_APP=src
ENV FLASK_ENV=development

WORKDIR /

# comment CMD and uncomment entry point if want to use container as interactive
CMD flask run --host 0.0.0.0

#ENTRYPOINT [ "/bin/bash" ]