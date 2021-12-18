FROM python:3.10-bullseye
COPY ./python /python
WORKDIR /python
# Install required Python module
RUN pip install speedtest-cli
RUN python ./tester.py
