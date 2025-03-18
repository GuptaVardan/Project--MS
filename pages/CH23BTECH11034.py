import streamlit as st

# Set page configuration
st.set_page_config(page_title="Selenium Properties", layout="wide")

# Load CSS
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Title
st.title("selenium Properties 🌟")

st.image("assets/selenium.png", width=200) 
# Background Image
st.markdown(f"""
<style>
    body {{
        background-image: url("https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/Selenium_atom.svg/1024px-Selenium_atom.svg.png");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
</style>
""", unsafe_allow_html=True)

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
    st.write("- Atomic Number: 34 🧮")
    st.write("- Atomic Mass: 78.96 ⚖️")
    st.write("- Electronic Configuration: [Ar] 3d¹⁰ 4s² 4p⁴ 💻")
    st.write("- Isotopes: Seven naturally occurring isotopes 🌍")

with tab2:
    st.write("### Physical Properties")
    st.write("- Appearance: Silvery or red 🎨")
    st.write("- Melting Point: 221°C 🔥")
    st.write("- Boiling Point: 685°C 💨")
    st.write("- Density: 4.81 g/cm³ 📏")
    st.write("- Atomic Radius: 120 pm ⚛️")
    st.write("- Crystal Structure: Hexagonal (gray form) 🧊")

with tab3:
    st.write("### Chemical Properties")
    st.write("- Electronegativity: 2.55 (Pauling scale) ⚡")
    st.write("- Oxidation States: -2, +4, +6 🔄")
    st.write("- Reactivity: Forms compounds with metals and nonmetals ⚗️")
    st.write("- Ionization Energies:")
    st.write("   - First: 941 kJ/mol 💡")
    st.write("   - Second: 2045 kJ/mol 💡")
    st.write("   - Third: 2973.7 kJ/mol 💡")

with tab4:
    st.write("### Quantum Properties")
    st.write("- Principal Quantum Number (n): 1 to 4 🔮")
    st.write("- Azimuthal Quantum Number (l): 0, 1, 2, 3 🔮")
    st.write("- Magnetic Quantum Number (mₗ): -l to +l 🔮")
    st.write("- Spin Quantum Number (mₛ): ±1/2 🔮")

with tab5:
    st.write("### Mechanical Properties")
    st.write("- Elasticity: Brittle 💔")
    st.write("- Plasticity: Not applicable (since it's brittle) 🚫")
    st.write("- Toughness/Ductility: Low toughness 🤏")

with tab6:
    st.write("### Electromagnetic Properties")
    st.write("- Electrical Conductivity: Low conductivity ⚡")
    st.write("- Magnetic Moment: Not significant 🧲")
    st.write("- Emission Spectrum: Not applicable 🌈")

with tab7:
    st.write("### Thermodynamic Properties")
    st.write("- Specific Heat Capacity (Cp): 25.04 J/(mol·K) 🌡️")
    st.write("- Heat of Fusion: 5.4 kJ/mol 🔥")
    st.write("- Enthalpy of Vaporization: 26 kJ/mol 💨")

with tab8:
    st.write("### Nuclear Properties")
    st.write("- Nuclear Spin (I): Not applicable ⚛️")
    st.write("- Binding Energy: Energy needed to hold the nucleus together 🔗")

with tab9:
    st.write("### Relativistic Properties")
    st.write("- Time Dilation Effects: Not significant at atomic scale 🕒")

# Additional Details
st.header("### Additional Details 📚")
st.markdown("""
- Selenium exhibits **photoconductivity**, increasing its conductivity when exposed to light 🌞.
- It plays a crucial role in the **semiconductor industry** due to its unique electrical properties ⚡.
- Selenium is used in **glass decolorization** and as a pigment for red glass 🎨.
""")

st.subheader("Orbital Simulation Diagram")
st.image("https://www.chemguide.co.uk/atoms/properties/sep.gif", caption="Selenium Orbital Diagram Example")

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
svg_file_path = "assets/bohr-animated (2).svg"  # Adjust path as needed
try:
    render_svg(svg_file_path)
except FileNotFoundError:
    st.error(f"SVG file not found at: {svg_file_path}")
