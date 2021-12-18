FROM python:3.7-bullseye
WORKDIR /usr/src/app
COPY ./python .
# Install required Python module
RUN pip3 install speedtest-cli
RUN python ./tester.py
