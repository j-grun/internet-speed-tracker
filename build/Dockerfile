FROM python:3.7-bullseye
WORKDIR /usr/src/app
COPY ./python .
# Install required Python module
RUN pip install --upgrade pip
RUN pip install speedtest
RUN python ./tester.py
