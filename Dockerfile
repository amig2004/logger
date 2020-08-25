FROM python:3.8-slim

# prepare env
COPY requirements.txt /root/requirements.txt
RUN pip install -r requirements.txt

# prepare backend app files
WORKDIR /backend
COPY __init__.py /backend/__init__.py
COPY database.py /backend/database.py

COPY main.py /backend/main.py
COPY tags.py /backend/tags.py


#configuration file
COPY config.json /backend/config.json

#prepare environment vars
ENV FLASK_APP=src
ENV FLASK_ENV=development

# expose port
EXPOSE 5000

# comment CMD and uncomment entry point if want to use container as interactive
CMD flask run

#ENTRYPOINT [ "/bin/bash" ]