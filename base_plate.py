"""Base plate with M6 mounting holes on 25mm grid."""

from build123d import *
from ocp_vscode import show

# Parameters
DIAMETER = 149.0
THICKNESS = 6.0
GRID_SPACING = 25.0
EDGE_MARGIN = 12.5
M6_TAP_DIA = 5.0


def grid_positions(diameter, spacing, margin):
    """Generate positions for circular grid pattern."""
    max_r = diameter / 2 - margin
    extent = int(max_r / spacing) + 1
    positions = []
    for i in range(-extent, extent + 1):
        for j in range(-extent, extent + 1):
            x, y = i * spacing, j * spacing
            if (x**2 + y**2) ** 0.5 <= max_r:
                positions.append((x, y))
    return positions


holes = grid_positions(DIAMETER, GRID_SPACING, EDGE_MARGIN)

with BuildPart() as model:
    with BuildSketch():
        Circle(DIAMETER / 2)
    extrude(amount=THICKNESS)

    with BuildSketch(model.faces().sort_by(Axis.Z)[-1]):
        for x, y in holes:
            with Locations([(x, y)]):
                Circle(M6_TAP_DIA / 2)
    extrude(amount=-THICKNESS, mode=Mode.SUBTRACT)

    for face in [model.faces().sort_by(Axis.Z)[-1], model.faces().sort_by(Axis.Z)[0]]:
        chamfer(face.outer_wire().edges(), length=0.8)

part = model.part

if __name__ == "__main__":
    print(f"Base plate: Ø{DIAMETER}mm, {len(holes)} M6 holes")

    try:
        show(part)
    except Exception:
        pass

    export_step(part, "exports/base_plate.step")
    export_stl(part, "exports/base_plate.stl")
    export_brep(part, "exports/base_plate.brep")
    print("Exported to exports/")
