import streamlit as st
import base64
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Set page configuration
st.set_page_config(page_title="Saragadam Lokesh-Zirconium Properties", layout="wide")

# Load CSS
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Title and Header
st.title("Zirconium Properties 🌟")
st.image("assets/Zirconium.png", width=200)

# Create tabs with new additions
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab12, tab13, tab14,tab15,tab16 = st.tabs([
    "🔍 Fundamental", "🔩 Physical", "⚗ Chemical", "🔮 Quantum", "💪 Mechanical",
    "🔌 Electromagnetic", "🌡 Thermodynamic", "⚛ Nuclear", "🕳 Relativistic",
    "🏭 Applications", "🌌 Astrophysics", "🔬 Crystallography", "⛰ Geological", "⚙ Alloys","🔬 XRD","🌀 3D Model"
])


with tab15:
    st.header("X-ray Diffraction (XRD) Pattern")
    st.write("X-ray source: Mo Kα (Molybdenum K-alpha, λ ≈ 0.7107 Å")
    st.markdown("""
    - *Material:* Zirconium (Zr)
    - *Crystal Structure:* Hexagonal Close-Packed (HCP)
    - *Key Peaks:* Corresponding to major diffraction angles (2θ)
    """)
    
    st.image("assets/Zirconium_xrd.jpg", caption="XRD Pattern of Zirconium", use_column_width=True)

# New Tabs with Added Properties
with tab10:  # Applications
    st.header("Industrial Applications")
    st.markdown("""
    *Nuclear Reactors*:
    - Neutron transparency: 0.18 barn absorption cross-section
    - Fuel rod cladding in PWR reactors
    
    *Advanced Materials*:
    - Zircaloy alloys (Zr + 1.5% Sn)
    - Superconducting ZrNb alloys (<4K)
    """)

with tab11:  # Astrophysics
    st.header(" Stellar Nucleosynthesis")
    st.markdown("""
    - *Formation Sites*:
      - s-process in AGB stars
      - r-process in supernovae
    - *Key Isotope*: Zr-90 (magic 50 neutrons)
    - Found in presolar grains 🌌
    """)

with tab12:  # Crystallography
    st.header("Crystal Structure Details")
    st.markdown("""
    *HCP Structure*:
    - Miller Indices: (0001), (10-10)
    - Lattice Constants: a = 3.23Å, c = 5.15Å
    
    *Dislocation Types*[14]:
    - Edge (1.2nm spacing)
    - Screw (0.8nm Burgers vector)
    """)

with tab13:  # Geological
    st.header(" Natural Occurrence")
    st.markdown("""
    - *Primary Mineral*: Zircon (ZrSiO₄)
    - Gemstone Varieties:
      - Hyacinth (red)
      - Jargon (colorless)
    - Global Reserves: ~60 million metric tons
    """)

with tab14:  # Alloys
    st.header("Alloy Properties")
    st.markdown("""
    *Zircaloy Composition*:
    
    zircaloy = {
        'Zr': 98%,
        'Sn': 1.5%,
        'Fe': 0.2%,
        'Cr': 0.1%
    }
    
    *Key Features*:
    - Corrosion resistance <300°C
    - Thermal neutron cross-section: 0.22 barns
    """)

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



# Bohr Model Section Remains
def render_svg(svg_file_path):
    with open(svg_file_path, "r") as f:
        svg_content = f.read()
    b64 = base64.b64encode(svg_content.encode("utf-8")).decode("utf-8")
    st.markdown(f'<img src="data:image/svg+xml;base64,{b64}"/>', unsafe_allow_html=True)

st.subheader("Orbital Simulation Diagram")
render_svg("assets/bohr-animated.svg")
# Display properties in tabs
# Updated Existing Tabs
with tab1:  # Fundamental
    st.header("Fundamental Properties")
    st.write("- Magic Number Isotope: Zr-90 (50 neutrons)")
    st.write("- Stable Isotopes: Zr-90, Zr-91, Zr-92, Zr-94")

    st.write("- Atomic Number: 40")
    st.write("- Atomic Mass: 91.22")
    st.write("- Electronic Configuration: [Kr] 4d² 5s²")
    st.write("- Isotopes: Five naturally occurring isotopes")

with tab2:  # Physical
    st.header("Physical Properties")
    st.write("- Appearance: Greyish-white")
    st.write("- Melting Point: 1853°C")
    st.write("- Boiling Point: 4400°C")
    st.write("- Density: 6.49 g/cm³")
    st.write("- Atomic Radius: 160 pm")
    st.write("- Crystal Structure: Hexagonal close-packed")
    st.write("- Phase Changes: HCP <863°C → BCC >863°C")
    st.write("- Anisotropic: Direction-dependent properties")

with tab3:
    st.header(" Chemical Properties")
    st.write("- Electronegativity: 1.33")
    st.write("- Oxidation State: +4")
    st.write("- Reactivity: Highly resistant to corrosion")
    st.write("- Ionization Energies:")
    st.write(" - First: 640.1 kJ/mol")
    st.write(" - Second: 1270 kJ/mol")
    st.write(" - Third: 2218 kJ/mol")

with tab4:
    st.header(" Quantum Properties")
    st.write("- Principal Quantum Number (n): 1 to 5")
    st.write("- Azimuthal Quantum Number (l): 0, 1, 2, 3")
    st.write("- Magnetic Quantum Number (mₗ): -l to +l")
    st.write("- Spin Quantum Number (mₛ): ±1/2")

with tab5:
    st.header(" Mechanical Properties")
    st.write("- Elasticity: Ductile and malleable")
    st.write("- Toughness/Ductility: High toughness")

with tab6:
    st.header(" Electromagnetic Properties")
    st.write("- Electrical Conductivity: Moderate conductivity")

with tab7:
    st.header(" Thermodynamic Properties")
    st.write("- Specific Heat Capacity (Cp): 25.36 J/(mol·K)")

# Updated Nuclear Properties Tab
with tab8:  # Nuclear
    st.header(" Nuclear Properties")
    st.markdown("""
    - *Radioactive Isotopes*:
      - Zr-93: Half Life - 1.53 million years (β⁻ → Nb-93)
      - Zr-95: Half Life - 64 days (β⁻ → Nb-95)
    - *Decay Chains*:
      
      graph LR
          Zr-95 -->|β⁻| Nb-95
          Nb-95 -->|β⁻| Mo-95
      
    """)
    st.write("- Binding Energy: Energy needed to hold the nucleus together")


