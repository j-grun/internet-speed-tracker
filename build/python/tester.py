import speedtest
from time import sleep

st = speedtest.Speedtest()

while TRUE:
  st.get_best_server()
  st.download()
  st.upload()
  sleep(60)
