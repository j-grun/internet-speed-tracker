FROM python:3.7-bullseye
WORKDIR /usr/src/app
COPY ./python .
# Install required Python module
RUN easy_install speedtest-cli
RUN python ./tester.py
