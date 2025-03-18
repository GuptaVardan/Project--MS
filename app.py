import streamlit as st

st.set_page_config(page_title="Material Science Assignment", layout="wide")

# Load CSS
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Title
st.title("Material Science Assignment")

# Header
st.header("Choose Student:")

# Layout for page links
col1, col2, col3 = st.columns(3)

with col1:
    st.page_link("pages/CH23BTECH11034.py", label="CH23BTECH11034 (Rahul Patil)")

with col2:
    st.page_link("pages/CH23BTECH11040.py", label="CH23BTECH11040 (Saragadam Lokesh)")

with col3:
    st.page_link("pages/CH23BTECH11044.py", label="CH23BTECH11044 (Vardan Gupta)")
