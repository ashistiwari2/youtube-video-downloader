from pytube import YouTube
import streamlit as st
from time import sleep

with st.form(key='youtube', clear_on_submit=True):
    link = st.text_area("Enter Youtube video link:", key='user')
    submit_text = st.form_submit_button(label='Submit')
try:
    yt = YouTube(link)
except:
    st.warning('--Invalid link---')
    ph = st.empty()
    N = 10
    bar = st.progress(0)
    for secs in range(0, N, 1):
        mm, ss = (N - secs) // 60, (N - secs) % 60
        bar.progress((secs + 1) * 10)
        ph.metric("Redirecting in...", f"{mm:02d}:{ss:02d}")
        sleep(1)

    st.experimental_rerun()


# link = input(" ")

# To print title
st.write("Title :{}".format(yt.title))
# print("Title :", yt.title)
# # To get number of views
# print("Views :", yt.views)
# # To get the length of video
# print("Duration :", yt.length)
# # To get description
# print("Description :", yt.description)
# # To get ratings
# print("Ratings :", yt.rating)
# stream = yt.streams.get_highest_resolution()
# stream.download()
# print("Download completed!!")
