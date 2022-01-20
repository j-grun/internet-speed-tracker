import speedtest
from time import sleep

st = speedtest.Speedtest()

while True:
  st.get_best_server()
  st.download()
  st.upload()
  sleep(60)
