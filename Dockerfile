FROM python:3.8-slim

# prepare env
COPY requirements.txt /root/requirements.txt
RUN pip install -r requirements.txt

# prepare backend app
WORKDIR /backend
COPY views /backend/views
COPY main.py /backend/main.py
COPY config.json /backend/config.json

#prepare environment vars
ENV flask_app=main.py

# expose port
EXPOSE 5000

CMD python main.py

#ENTRYPOINT [ "/bin/bash" ]