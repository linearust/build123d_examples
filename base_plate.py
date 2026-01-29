from build123d import *

D, T, G, M = 149, 6, 25, 12.5  # diameter, thickness, grid, margin
r = D / 2 - M
holes = [(i * G, j * G) for i in range(-3, 4) for j in range(-3, 4) if (i * G) ** 2 + (j * G) ** 2 <= r**2]

with BuildPart() as p:
    Cylinder(D / 2, T)
    with BuildSketch(p.faces().sort_by(Axis.Z)[-1]):
        with Locations(holes):
            Circle(2.5)
    extrude(amount=-T, mode=Mode.SUBTRACT)
    edges = p.edges().filter_by(GeomType.CIRCLE).sort_by(SortBy.RADIUS)[-2:]
    chamfer(edges, 0.8)

part = p.part

if __name__ == "__main__":
    export_step(part, "exports/base_plate.step")
    export_stl(part, "exports/base_plate.stl")
    export_brep(part, "exports/base_plate.brep")
