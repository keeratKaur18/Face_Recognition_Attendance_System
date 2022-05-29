import streamlit as st
import requests
from streamlit_lottie import st_lottie
import pyttsx3

st.set_page_config(page_title="FACE RECOGNITION ATTENDANCE", page_icon=":camera:", layout="wide")
st.subheader("Welcome! :wave: ")

def load_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# loading assets
lottie_asset = load_url("https://assets6.lottiefiles.com/packages/lf20_m9ub4f.json")

left_col, right_col = st.columns(2)
with left_col:
    st.title("Face Recognition Attendance System")
with right_col:
    st_lottie(lottie_asset, height=150)

# removing footer and hamburger button icon
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

webframe = st.image([])        # variable to make camera visible on web page
st.write('---')
result = st.button('DISPLAY ATTENDANCE')     # button to print names with respective time of arrival

sound = pyttsx3.init()
sound.say('welcome')
sound.runAndWait()