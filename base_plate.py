"""
Base Plate for Drone Payload Mounting
=====================================
Simple circular plate with M6 holes on 25mm grid.
"""

from build123d import *
from ocp_vscode import show

# ============================================================
# Parameters (all dimensions in mm)
# ============================================================

# Plate dimensions
PLATE_DIAMETER = 149.0
PLATE_THICKNESS = 6.0

# Grid pattern
GRID_SPACING = 25.0
EDGE_MARGIN = 12.5

# M6 tapped holes
M6_TAP_DIAMETER = 5.0  # Pilot hole for M6x1.0 tap

# ============================================================
# Calculate hole positions
# ============================================================

def get_grid_positions(diameter, spacing, margin):
    """Calculate positions for a circular grid pattern."""
    max_radius = diameter / 2 - margin
    positions = []

    max_extent = int(max_radius / spacing) + 1

    for i in range(-max_extent, max_extent + 1):
        for j in range(-max_extent, max_extent + 1):
            x = i * spacing
            y = j * spacing
            radius = (x**2 + y**2)**0.5

            if radius <= max_radius:
                positions.append((x, y))

    return positions

hole_positions = get_grid_positions(PLATE_DIAMETER, GRID_SPACING, EDGE_MARGIN)

print(f"M6 holes: {len(hole_positions)} places")

# ============================================================
# Build the base plate
# ============================================================

with BuildPart() as base_plate:
    # Main circular plate
    with BuildSketch():
        Circle(PLATE_DIAMETER / 2)
    extrude(amount=PLATE_THICKNESS)

    top_face = base_plate.faces().sort_by(Axis.Z)[-1]

    # Create M6 tapped holes
    with BuildSketch(top_face):
        for x, y in hole_positions:
            with Locations([(x, y)]):
                Circle(M6_TAP_DIAMETER / 2)

    extrude(amount=-PLATE_THICKNESS, mode=Mode.SUBTRACT)

    # Chamfer outer edges
    top_face = base_plate.faces().sort_by(Axis.Z)[-1]
    bottom_face = base_plate.faces().sort_by(Axis.Z)[0]
    chamfer(top_face.outer_wire().edges(), length=0.8)
    chamfer(bottom_face.outer_wire().edges(), length=0.8)

# ============================================================
# Output
# ============================================================

part = base_plate.part

print("=" * 50)
print(f"Diameter: Ø{PLATE_DIAMETER} mm")
print(f"Grid spacing: {GRID_SPACING} mm")
print(f"M6 holes: {len(hole_positions)} places")
print("=" * 50)

try:
    show(part)
except Exception as e:
    print(f"\nViewer not available: {e}")

from build123d import export_step, export_stl, export_brep
export_step(part, "base_plate.step")
export_stl(part, "base_plate.stl")
export_brep(part, "base_plate.brep")
print("\nExported to: base_plate.step, base_plate.stl, base_plate.brep")
