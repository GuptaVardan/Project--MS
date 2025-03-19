import streamlit as st
import base64
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Set page configuration
st.set_page_config(page_title="Rahul Patil-Selenium Properties", layout="wide")

# Load CSS
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Title and Header
st.title("Selenium Properties 🌟")
st.image("assets/selenium.png", width=200)


# Create tabs with new additions
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab12, tab13, tab14 ,tab15, tab16= st.tabs([
    "🔍 Fundamental", "🔩 Physical", "⚗ Chemical", "🔮 Quantum", "💪 Mechanical",
    "🔌 Electromagnetic", "🌡 Thermodynamic", "⚛ Nuclear", "🕳 Relativistic",
    "🔲 Allotropes", "☠ Toxicity", "🌌 Astrophysics", "💡 Applications", "🔬 Crystallography","🔬 XRD","🌀 3D Model"
])
with tab15:
    st.header("X-ray Diffraction (XRD) Pattern")
    st.write("X-ray source: Cu Kα (Copper K-alpha, λ ≈ 1.5406 Å)")
    st.markdown("""
    - *Material:* Selenium (Se)
    - *Crystal Structure:* Hexagonal Close-Packed (HCP)
    - *Key Peaks:* Corresponding to major diffraction angles (2θ)
    """)
    
    st.image("assets/Selenium_xrd.jpg", caption="XRD Pattern of Selenium", use_column_width=True)
# Display properties in tabs
with tab1:
    st.header(" Fundamental Properties")
    st.write("- Atomic Number: 34")
    st.write("- Stable Isotopes: ⁷⁴Se, ⁷⁶Se, ⁷⁷Se, ⁷⁸Se, ⁸⁰Se")
    st.write("- Radioactive Isotopes: ⁷⁵Se (119.8d), ⁷⁹Se (327ka)")

    st.write("- Atomic Mass: 78.96")
    st.write("- Electronic Configuration: [Ar] 3d¹⁰ 4s² 4p⁴")
    st.write("- Isotopes: Seven naturally occurring isotopes")
with tab8:
    st.header("Nucleare properties")
    st.markdown("""
    - *Radioactive Isotopes*:
      - Se-75: Half Life - 119.8 days (β⁻ decay) → As-75 (Stable)
      - Se-79: Half Life - 327,000 years (β⁻ decay) → Br-79 (Stable)
    
      
    """)
with tab2:
    st.header(" Physical Properties")
    st.write("- Appearance: Silvery or red")
    st.write("- Melting Point: 221°C")
    st.write("- Boiling Point: 685°C")
    st.write("- Density: 4.81 g/cm³")
    st.write("- Anisotropic: Different properties along crystal axes")

    st.write("- Atomic Radius: 120 pm")
    st.write("- Crystal Structure: Hexagonal (gray form)")

with tab3:
    st.header("Chemical Properties")
    st.write("- Electronegativity: 2.55 (Pauling scale)")
    st.write("- Oxidation States: -2, +4, +6")
    st.write("- Reactivity: Forms compounds with metals and nonmetals")
    st.write("- Ionization Energies:")
    st.write("   - First: 941 kJ/mol")
    st.write("   - Second: 2045 kJ/mol")
    st.write("   - Third: 2973.7 kJ/mol")

with tab4:
    st.header(" Quantum Properties")
    st.write("- Principal Quantum Number (n): 1 to 4")
    st.write("- Azimuthal Quantum Number (l): 0, 1, 2, 3")
    st.write("- Magnetic Quantum Number (mₗ): -l to +l")
    st.write("- Spin Quantum Number (mₛ): ±1/2")

with tab5:
    st.header(" Mechanical Properties")
    st.write("- Elasticity: Brittle")
    st.write("- Plasticity: Not applicable (since it's brittle)")
    st.write("- Toughness/Ductility: Low toughness")

with tab6:
    st.header("Electromagnetic Properties")
    st.write("- Electrical Conductivity: Low conductivity")
    st.write("- Magnetic Moment: Not significant")
    st.write("- Emission Spectrum: only UV and X-ray region")

with tab7:
    st.header("Thermodynamic Properties")
    st.write("- Specific Heat Capacity (Cp): 25.04 J/(mol·K)")
    st.write("- Heat of Fusion: 5.4 kJ/mol")
    st.write("- Enthalpy of Vaporization: 26 kJ/mol")

with tab16:
    st.header("3D Model Visualization")
    
    def hexagonal_lattice_3d(rows, cols, layers, spacing=1.0):
        """Generate a 3D hexagonal lattice structure."""
        points = []
        
        for z in range(layers):
            for row in range(rows):
                for col in range(cols):
                    x = col * spacing * np.sqrt(3)
                    y = row * spacing * 1.5
                    if col % 2 == 1:
                        y += spacing * 0.75  # Offset for hexagonal tiling
                    points.append((x, y, z * spacing))  # Add third dimension (z-layer)

        return np.array(points)

    # Generate hexagonal lattice
    rows, cols, layers = 5, 5, 3  # Modify these for different lattice sizes
    points = hexagonal_lattice_3d(rows, cols, layers)

    # Create figure and 3D axes
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Plot points
    ax.scatter(points[:, 0], points[:, 1], points[:, 2], color='blue', s=60)

    # Connect neighboring points to create a lattice effect
    edges = []
    spacing = 1.0 * np.sqrt(3)  # Hexagonal spacing

    for i, (x, y, z) in enumerate(points):
        for j, (x2, y2, z2) in enumerate(points):
            dist = np.linalg.norm([x - x2, y - y2, z - z2])
            if 0 < dist < spacing * 1.1:  # Connect nearest neighbors
                edges.append(([x, x2], [y, y2], [z, z2]))

    for edge in edges:
        ax.plot(edge[0], edge[1], edge[2], color='gray', linewidth=1)

    # Customize appearance
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_zlabel("Z-axis")
    ax.set_title("3D Hexagonal Lattice")
    ax.set_box_aspect([1, 1, 0.6])
    
    st.pyplot(fig)

# Additional Details

st.header(" Additional Details 📚")

st.markdown("""
- Selenium exhibits **photoconductivity**, increasing its conductivity when exposed to light.
- It plays a crucial role in the **semiconductor industry** due to its unique electrical properties.
- Selenium is used in **glass decolorization** and as a pigment for red glass.
""")


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
st.write("Below is an animated Bohr model representation of Selenium:")

# Render the SVG file directly (ensure the file exists in your project directory)
svg_file_path = "assets/bohr-animated (2).svg"  # Adjust path as needed
try:
    render_svg(svg_file_path)
except FileNotFoundError:
    st.error(f"SVG file not found at: {svg_file_path}")


with tab10:  # Allotropes
    st.header("Allotropic Forms")
    st.markdown("""
    *Crystalline Forms*:
    - Gray Selenium (Hexagonal, Metallic)
    - Red Selenium (Monoclinic)
    
    *Amorphous Forms*:
    - Black Selenium (Vitreous)
    - Colloidal Red (Nanoparticles)
    """)

with tab11:  # Toxicity
    st.header("Toxicological Profile")
    st.markdown("""
    - *LD₅₀ (Human)*: ~5mg/kg
    - *Acute Symptoms*: Respiratory distress, garlic breath
    - *Chronic Exposure*: Hair loss, neurological damage
    """)

with tab12:  # Astrophysics
    st.header("Supernova Nucleosynthesis")
    st.markdown("""
    - *Formation Process*:
      - r-process in Type II supernovae
      - Neutron star mergers
    - *Key Isotopes*: ⁷⁷Se, ⁷⁸Se, ⁸²Se
    """)

with tab13:  # Applications
    st.header("Industrial Applications")
    st.markdown("""
    - *Semiconductor Uses*:
      - Solar cells
      - Quantum dot LEDs
    """)


with tab14:  # Crystallography
    st.header("Crystalline Properties")
    st.markdown("""
    *Hexagonal Structure*:
    - Miller Indices: (0001), (101̅0)
    - Dislocation Types: Edge & Screw[14]
    - Lattice Constants: a=4.36Å, c=4.95Å
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