import speedtest

st = speedtest.Speedtest()
st.get_best_server()
st.download()
st.upload()
