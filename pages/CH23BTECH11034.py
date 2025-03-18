# CH23BTECH11034.py
import streamlit as st

st.set_page_config(page_title="Rahul Patil - Selenium", layout="wide")

# Load CSS
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("Assignment: Rahul Patil (Roll No. CH23BTECH11034)")

st.header("Element: Selenium (Atomic Number 34)")

st.subheader("Fundamental Properties")
st.markdown("""
- **Atomic Mass:** 78.96 u  
- **Electronic Configuration:** [Ar] 3d¹⁰ 4s² 4p⁴  
- **Isotopes:** Seven naturally occurring isotopes  
""")

st.subheader("Physical Properties")
st.markdown("""
- **Appearance:** Silvery or red  
- **Melting Point:** 221°C  
- **Boiling Point:** 685°C  
- **Density:** 4.81 g/cm³  
- **Crystal Structure:** Hexagonal (gray form), Monoclinic (red), Amorphous (black)
""")

st.subheader("Chemical Properties")
st.markdown("""
- **Electronegativity:** 2.55  
- **Oxidation States:** -2, +4, +6  
- **Reactivity:** Forms compounds with metals and nonmetals.
""")

st.subheader("Special Properties")
st.markdown("""
- Exhibits photoconductivity, used in photocells and solar panels.
- Toxic in high doses causing selenosis.
""")

st.subheader("Orbital Simulation Diagram")
st.image("https://www.chemguide.co.uk/atoms/properties/sep.gif", caption="Selenium Orbital Diagram Example")
