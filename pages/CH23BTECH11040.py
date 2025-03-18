# CH23BTECH11040.py
import streamlit as st

st.set_page_config(page_title="Saragadam Lokesh - Zirconium", layout="wide")

# Load CSS
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("Assignment: Saragadam Lokesh (Roll No. CH23BTECH11040)")

st.header("Element: Zirconium (Atomic Number 40)")

st.subheader("Fundamental Properties")
st.markdown("""
- **Atomic Mass:** 91.22 u  
- **Electronic Configuration:** [Kr] 4d² 5s²  
- **Isotopes:** Five naturally occurring isotopes  
""")

st.subheader("Physical Properties")
st.markdown("""
- **Appearance:** Greyish-white  
- **Melting Point:** 1853°C  
- **Boiling Point:** 4400°C  
- **Density:** 6.49 g/cm³  
- **Crystal Structure:** Hexagonal close-packed (HCP), BCC at high temperatures (>863°C)
""")

st.subheader("Chemical Properties")
st.markdown("""
- **Electronegativity:** 1.33  
- **Oxidation State:** +4  
- Highly resistant to corrosion.
""")

st.subheader("Special Properties")
st.markdown("""
- High neutron transparency used in nuclear reactor cladding.
- Exhibits superconductivity at extremely low temperatures.
""")

st.subheader("Orbital Simulation Diagram")
st.image("https://www.chemguide.co.uk/atoms/properties/zrp.gif", caption="Zirconium Orbital Diagram Example")
