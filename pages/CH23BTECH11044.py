import streamlit as st

st.set_page_config(page_title="Vardan Gupta - Ruthenium", layout="wide")

# Load CSS
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("Assignment: Vardan Gupta (Roll No. CH23BTECH11044)")

st.header("Element: Ruthenium (Atomic Number 44)")

st.subheader("Fundamental Properties")
st.markdown("""
- **Atomic Mass:** 101.1 u  
- **Electronic Configuration:** [Kr] 4d⁷ 5s¹  
- **Isotopes:** Seven naturally occurring isotopes  
""")

st.subheader("Physical Properties")
st.markdown("""
- **Appearance:** Silver shiny metal  
- **Melting Point:** 2250°C  
- **Boiling Point:** 4150°C  
- **Density:** 12.2 g/cm³  
- **Crystal Structure:** Hexagonal close-packed (HCP)
""")

st.subheader("Chemical Properties")
st.markdown("""
- **Electronegativity:** 2.2  
- **Oxidation States:** +3, +4, +8  
- Highly resistant to corrosion and acids.
""")

st.subheader("Special Properties")
st.markdown("""
- Effective catalyst in hydrogenation reactions and ammonia production.
- Used in magnetic storage technology for hard-disk drives.
""")

st.subheader("Orbital Simulation Diagram")
st.image("https://www.chemguide.co.uk/atoms/properties/rup.gif", caption="Ruthenium Orbital Diagram Example")
