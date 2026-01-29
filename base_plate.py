from build123d import *

D, T, G, M = 149, 6, 25, 12.5
r = D / 2 - M
holes = [(i*G, j*G) for i in range(-3, 4) for j in range(-3, 4) if (i*G)**2 + (j*G)**2 <= r**2]

with BuildPart() as p:
    Cylinder(D/2, T)
    with BuildSketch(p.faces().sort_by(Axis.Z)[-1]):
        with Locations(holes):
            Circle(2.5)
    extrude(amount=-T, mode=Mode.SUBTRACT)
    chamfer(p.edges().filter_by(GeomType.CIRCLE).sort_by(SortBy.RADIUS)[-2:], 0.8)

part = p.part

if __name__ == "__main__":
    for fmt in [export_step, export_stl, export_brep]:
        fmt(part, f"exports/base_plate.{fmt.__name__.split('_')[1]}")
