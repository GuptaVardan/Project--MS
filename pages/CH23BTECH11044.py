import streamlit as st
import base64

# Set page configuration
st.set_page_config(page_title="Vardan Gupta-Ruthenium Properties", layout="wide")

# Load CSS
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


st.title("Ruthenium Properties 🌟")
st.image("assets/ruthenium.png", width=200)

# Create tabs with new additions
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab12, tab13,tab14 = st.tabs([
    "🔍 Fundamental", "🔩 Physical", "⚗ Chemical", "🔮 Quantum", "💪 Mechanical",
    "🔌 Electromagnetic", "🌡 Thermodynamic", "⚛ Nuclear", "🕳 Relativistic",
    "🏭 Applications", "🌌 Astrophysics", "💎 Jewelry", "🔬 Crystallography","🔬 XRD"
])

# Updated Existing Tabs
with tab14:
    st.header("X-ray Diffraction (XRD) Pattern")
    st.write("X-ray source: Co Kα (Cobalt K-alpha, λ ≈ 1.7889 Å)")
    st.markdown("""
    - *Material:* Ruthenium (Ru)
    - *Crystal Structure:* Hexagonal Close-Packed (HCP)
    - *Key Peaks:* Corresponding to major diffraction angles (2θ)
    """)
    
    st.image("assets/Ruthenium_xrd.jpg", caption="XRD Pattern of Ruthenium", use_container_width=True)



# New Tabs with Added Properties
with tab10:  # Applications
    st.header("Industrial Applications")
    st.markdown("""
    *Catalysis*:
    - Ammonia synthesis (Haber process)
    - Oxygen evolution reaction (OER) in water splitting
    
    def calculate_activity(surface_area):
        return base_activity * (surface_area/100)
    
    
    *Data Storage*:
    - Perpendicular magnetic recording layers
    - 1.2TB/inch² density in modern HDDs
    """)

with tab11:  # Astrophysics
    st.header("Stellar Nucleosynthesis")
    st.markdown("""
    - *Formation Sites*:
      - r-process in neutron star mergers
      - Type Ia/II supernovae
    - *Key Isotopes*: Ru-99, Ru-106
    - Found in presolar meteorites 🌠
    """)

with tab12:  # Jewelry
    st.header("Jewelry Applications")
    st.markdown("""
    *Alloy Composition*:
    - Pt-Ru (95:5 ratio) increases hardness by 40%
    - Pd-Ru improves tarnish resistance
    
    *Plating Benefits*:
    - Scratch resistance: 9 Mohs scale
    - Color options: Light gray to black metallic
    """)

with tab13:  # Crystallography
    st.header("Crystal Structure Details")
    st.markdown("""
    *HCP Characteristics*:
    - Miller Indices: (0001), (10-10)
    - Dislocation Types: Screw (80% prevalence) 
    - Slip Systems: Basal ⟨a⟩ type
    
    *Mechanical Effects*:
    - Vickers Hardness: 800 HV (pure Ru)
    - Grain boundary strengthening effects
    """)

# Updated Nuclear Properties Tab
with tab8:  # Nuclear
    st.write("### Nuclear Properties")
    st.markdown("""
    - *Radioactive Isotopes*:
      - Ru-103: 39.26d (β⁻ → Rh-103)
      - Ru-106: 373.6d (β⁻ → Rh-106)
    - *Decay Chains*:
      
      graph LR
          Ru-106 --> Rh-106
          Rh-106 --> Pd-106
      
    - Neutron Cross Section: 2.6 barns (thermal)
    """)

# Background styling remains unchanged
st.markdown("""
<style>
    body {{
        background-image: url("https://upload.wikimedia.org/...");
        background-size: cover;
    }}
</style>
""", unsafe_allow_html=True)

# Bohr Model Section
def render_svg(svg_file_path):
    with open(svg_file_path, "r") as f:
        svg_content = f.read()
    b64 = base64.b64encode(svg_content.encode("utf-8")).decode("utf-8")
    st.markdown(f'<img src="data:image/svg+xml;base64,{b64}"/>', unsafe_allow_html=True)

st.subheader("Orbital Simulation Diagram")
render_svg("assets/bohr-animated (1).svg")
# Display properties in tabs
with tab1:  # Fundamental
    st.write("### Fundamental Properties")
    st.markdown("""
    - Atomic Number: 44 
    - Magic Number Isotope: Ru-94 (50 neutrons) ✅
    - Stable Isotopes: Ru-96, Ru-98, Ru-99, Ru-100, Ru-101, Ru-102, Ru-104
    - Electronic Configuration: [Kr] 4d⁷ 5s¹ 
    """)
    st.write("- Atomic Number: 44")
    st.write("- Atomic Mass: 101.1")
    st.write("- Electronic Configuration: [Kr] 4d⁷ 5s¹")
    st.write("- Isotopes: Seven naturally occurring isotopes.")

with tab2:  # Physical
    st.write("### Physical Properties")
    st.markdown("""
    - *Crystal Structure*: Hexagonal close-packed (HCP) 
    - Lattice Constants: a=270.59pm, c=428.15pm 
    - Anisotropic Properties: Electrical/mechanical direction-dependence 
    """)
    st.write("- Appearance: Silver shiny.")
    st.write("- Melting Point: 2250°C")
    st.write("- Boiling Point: 4150°C")
    st.write("- Density: 12.2 g/cm³")
    st.write("- Atomic Radius: 134 pm")
    st.write("- Crystal Structure: Hexagonal close-packed.")

with tab3:
    st.write("### Chemical Properties")
    st.write("- Electronegativity: 2.2 (Pauling scale)")
    st.write("- Oxidation States: +3, +4, +8")
    st.write("- Reactivity: Highly resistant to corrosion and acids.")
    st.write("- Ionization Energies: First: 710 kJ/mol, Second: 1620 kJ/mol, Third: 2747 kJ/mol")

with tab4:
    st.write("### Quantum Properties")
    st.write("- Principal Quantum Number (n): 1 to 5")
    st.write("- Azimuthal Quantum Number (l): 0, 1, 2, 3")
    st.write("- Magnetic Quantum Number (mₗ): -l to +l")
    st.write("- Spin Quantum Number (mₛ): ±1/2")
    st.write("- Quantum Number Range:")
    st.write("  - n: 1 to ∞")
    st.write("  - l: 0 to n-1")
    st.write("  - mₗ: -l to +l")
    st.write("  - mₛ: ±1/2")

with tab5:
    st.write("### Mechanical Properties")
    st.write("- Elasticity: Hard and brittle.")
    st.write("- Plasticity: Exhibits some plastic deformation.")
    st.write("- Toughness/Ductility: Low toughness.")

with tab6:
    st.write("### Electromagnetic Properties")
    st.write("- Electrical Conductivity: Moderate conductivity.")
    st.write("- Magnetic Moment: Not significant.")
    st.write("- Emission Spectrum: Not applicable.")
    st.write("- Polarizability: Not significant.")

with tab7:
    st.write("### Thermodynamic Properties")
    st.write("- Specific Heat Capacity (Cp): 24.06 J/(mol·K)")
    st.write("- Heat of Formation: Not applicable.")
    st.write("- Thermal Conductivity: 117 W/(m·K)")
    st.write("- Enthalpy of Fusion: 38.59 kJ/mol")
    st.write("- Enthalpy of Vaporization: 591.6 kJ/mol")

with tab8:
    st.write("### Nuclear Properties")
    st.write("- Nuclear Spin (I): Not applicable.")
    st.write("- Binding Energy: Energy needed to hold the nucleus together.")
    st.write("- Decay Mode: Not applicable.")
    st.write("- Neutron Cross-Section: Low probability of neutron capture.")

with tab9:
    st.write("Relativistic Properties")
    st.write("- Time Dilation Effects: Not significant at atomic scale.")
    st.write("- Relativistic Energy Correction: Electron energies shift slightly due to special relativity")

# Additional Details
st.write("\n")
st.header("Additional Details")
st.write("Ruthenium is a highly effective catalyst in hydrogenation reactions and ammonia production.")
st.write("It plays a role in magnetic storage technology for hard-disk drives.")
st.write("Ruthenium-based catalysts are used in water splitting for hydrogen fuel cells.")

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
st.write("Below is an animated Bohr model representation of Rythenium:")

# Render the SVG file directly (ensure the file exists in your project directory)
svg_file_path = "assets/bohr-animated (1).svg"  # Adjust path as needed
try:
    render_svg(svg_file_path)
except FileNotFoundError:
    st.error(f"SVG file not found at: {svg_file_path}")
