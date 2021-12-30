FROM python:latest
RUN pip install speedtest-cli
WORKDIR /usr/src/app
COPY ./python .
ENTRYPOINT ["python", "./tester.py"]
