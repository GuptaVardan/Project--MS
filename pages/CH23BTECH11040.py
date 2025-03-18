import streamlit as st

# Set page configuration
st.set_page_config(page_title="Zirconium Properties", layout="wide")

# Load CSS
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Title with an image
st.title("Zirconium Properties 🌟")
st.image("assets/Zirconium.png", width=200)

# Tabbed interface for properties
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10 = st.tabs([
    "🔍 Fundamental Properties",
    "🔩 Physical Properties",
    "⚗️ Chemical Properties",
    "🔮 Quantum Properties",
    "💪 Mechanical Properties",
    "🔌 Electromagnetic Properties",
    "🌡️ Thermodynamic Properties",
    "⚛️ Nuclear Properties",
    "🕳️ Relativistic Properties",
    "⚛️ Bohr Model Simulation"
])

# Display properties in tabs
with tab1:
    st.write("### Fundamental Properties")
    st.write("- Atomic Number: 40 🧮")
    st.write("- Atomic Mass: 91.22 ⚖️")
    st.write("- Electronic Configuration: [Kr] 4d² 5s² 💻")
    st.write("- Isotopes: Five naturally occurring isotopes 🌍")

with tab2:
    st.write("### Physical Properties")
    st.write("- Appearance: Greyish-white 🎨")
    st.write("- Melting Point: 1853°C 🔥")
    st.write("- Boiling Point: 4400°C 💨")
    st.write("- Density: 6.49 g/cm³ 📏")
    st.write("- Atomic Radius: 160 pm ⚛️")
    st.write("- Crystal Structure: Hexagonal close-packed 🧊")

with tab3:
    st.write("### Chemical Properties")
    st.write("- Electronegativity: 1.33 ⚡")
    st.write("- Oxidation State: +4 🔄")
    st.write("- Reactivity: Highly resistant to corrosion ⚗️")
    st.write("- Ionization Energies:")
    st.write(" - First: 640.1 kJ/mol 💡")
    st.write(" - Second: 1270 kJ/mol 💡")
    st.write(" - Third: 2218 kJ/mol 💡")

with tab4:
    st.write("### Quantum Properties")
    st.write("- Principal Quantum Number (n): 1 to 5 🔮")
    st.write("- Azimuthal Quantum Number (l): 0, 1, 2, 3 🔮")

with tab5:
    st.write("### Mechanical Properties")
    st.write("- Elasticity: Ductile and malleable 💪")
    st.write("- Toughness/Ductility: High toughness 🤏")

with tab6:
    st.write("### Electromagnetic Properties")
    st.write("- Electrical Conductivity: Moderate conductivity ⚡")

with tab7:
    st.write("### Thermodynamic Properties")
    st.write("- Specific Heat Capacity (Cp): 25.36 J/(mol·K) 🌡️")

with tab8:
    st.write("### Nuclear Properties")
    st.write("- Binding Energy: Energy needed to hold the nucleus together 🔗")

with tab9:
    st.write("### Relativistic Properties")
    st.write("- Time Dilation Effects: Not significant at atomic scale 🕒")

# Add Bohr Model Simulation Tab
# Streamlit interface for Bohr model simulation with animation
import base64

def render_svg(svg_file_path):
    """
    Reads and renders an SVG file in Streamlit.
    
    Parameters:
        svg_file_path (str): Path to the SVG file.
    """
    with open(svg_file_path, "r") as f:
        svg_content = f.read()  # Read the SVG file content
    b64 = base64.b64encode(svg_content.encode("utf-8")).decode("utf-8")
    html = r'<img src="data:image/svg+xml;base64,%s"/>' % b64
    st.write(html, unsafe_allow_html=True)

# Orbital Simulation Diagram Section
st.subheader("Orbital Simulation Diagram")
st.write("Below is an animated Bohr model representation of Zirconium:")

# Render the SVG file directly (ensure the file exists in your project directory)
svg_file_path = "assets/bohr-animated.svg"  # Adjust path as needed
try:
    render_svg(svg_file_path)
except FileNotFoundError:
    st.error(f"SVG file not found at: {svg_file_path}")
