from pytube import YouTube
import streamlit as st
from time import sleep
y=0
def Download(yt):
    DOWNLOAD_PATH = " C:/Users/" 
    mp4files = yt.filter('mp4')  
    yt.set_filename(yt.title)  
    d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution)  
    try:
        d_video.download(DOWNLOAD_PATH)
        st.success('Download started check your folder', icon="✅")
        
    except:
        st.warning("--Error has occured--")
        


with st.form(key='youtube', clear_on_submit=True):
    link = st.text_area("Enter Youtube video link:", key='user')
    link1=link
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
    link2=link.split('=')
    st.write(yt.thumbnail_url)
#     imgUrl = f"http://i.ytimg.com/vi/{link2[1]}/maxresdefault.jpg"
#     st.write(imgUrl)
    with st.spinner(f'Searching video on youtube for {link}.....'):
        col1, col2 = st.columns(2)
        sleep(8)
        with col1:
            st.image(yt.thumbnail_url, caption=yt.title, width=200, channels="RGB", output_format="auto")
            st.write("Title :{}".format(yt.title))
            st.write("Views :{}".format(yt.views))
            
        with col2:
            st.write("Duration:{}".format(yt.length))
            st.write("Descrption:{}".format(yt.description))
            st.write("Rating:{}".format(yt.rating))
     
     
    download = st.radio(
    "Do you want to download the video",
    ('Yes','No','rerun the app'))
    if download =='Yes':
        Download(yt)
        
    
    elif download=='No':
        st.write("You have selected no")
        
    elif download =='rerun the app':
        st.experimental_rerun()
    

        


