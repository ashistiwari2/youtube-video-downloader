from pytube import YouTube
import streamlit as st
from time import sleep
y=0

with st.form(key='youtube', clear_on_submit=True):
    link = st.text_area("Enter Youtube video link:", key='user')
    submit_text = st.form_submit_button(label='Submit')
if submit_text:
    try:
        yt = YouTube(link)
        y=1
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
        
        
if y==1:
    with st.spinner(f'Searching video on youtube for {link}.....'):
        col1, col2 = st.columns(2)
        sleep(8)
        with col1:
            st.write("Title :{}".format(yt.title))
            st.write("Views :{}".format(yt.views))
            st.write("Duration:{}".format(yt.length))
        with col2:
            st.write("Descrption:{}".format(yt.description))
            st.write("Rating:{}".format(yt.rating))
    
            
    
       
        
    
    



# link = input(" ")

# To print title

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
