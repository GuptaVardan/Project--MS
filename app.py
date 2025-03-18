import streamlit as st

# Set page configuration
st.set_page_config(page_title="Material Science Assignment", layout="wide")

# Load CSS
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Title
st.title("Material Science Assignment")

# Header
st.header("Choose Element:")

# Layout for element links
col1, col2, col3 = st.columns(3)

with col1:
    st.page_link("pages/CH23BTECH11034.py", label="Selenium (Atomic Number: 34)")

with col2:
    st.page_link("pages/CH23BTECH11040.py", label="Zirconium (Atomic Number: 40)")

with col3:
    st.page_link("pages/CH23BTECH11044.py", label="Ruthenium (Atomic Number: 44)")
