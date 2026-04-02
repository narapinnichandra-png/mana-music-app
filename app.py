import streamlit as st
import yt_dlp

st.set_page_config(page_title="MANA MUSIC APP", page_icon="🎧")

st.title("🎧 MANA MUSIC APP(online Music)")
st.write("Meeku nacchina paata peru type cheyandi bro!")

# Search Bar
search_query = st.text_input("Song Name Search Cheyandi:", placeholder="Example: OG...")

if st.button("Search & Play 🎶"):
    if search_query:
        try:
            with st.spinner('Internet lo vethiki, load chesthunnam...'):
                ydl_opts = {
                    'format': 'bestaudio/best',
                    'default_search': 'ytsearch',
                    'quiet': True,
                    'noplaylist': True
                }
                
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(f"ytsearch:{search_query}", download=False)['entries'][0]
                    audio_url = info['url']
                    title = info.get('title', 'Unknown Title')
                    thumbnail = info.get('thumbnail', '')

                if thumbnail:
                    st.image(thumbnail, width=300)
                
                st.subheader(f"🎵 Now Playing: {title}")
                st.audio(audio_url)
                st.balloons()
        except Exception as e:
            st.error("Paata dhorakaledhu bro, spelling check chesi malli try cheyi!")
    else:
        st.warning("Edo oka paata peru type chey bro!")
