# build123d Examples

Parametric CAD models using [build123d](https://github.com/gumyr/build123d).

## Setup

```bash
pip install nox uv
```

## Usage

```bash
nox -s run                    # Run default model
nox -s run -- base_plate.py   # Run specific model
nox -s export                 # Export all models
```

Outputs go to `exports/` (STEP, STL, BREP).

## Models

| Script | Description |
|--------|-------------|
| `base_plate.py` | Circular plate Ø149mm with M6 holes on 25mm grid |

## Live Preview

Use VS Code with [OCP CAD Viewer](https://marketplace.visualstudio.com/items?itemName=bernhard-42.ocp-cad-viewer).
