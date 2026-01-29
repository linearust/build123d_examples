# build123d Examples

Parametric CAD models using [build123d](https://github.com/gumyr/build123d).

## Setup

```bash
uv sync
```

## Run

```bash
uv run python base_plate.py
```

Exports STEP, STL, BREP to `exports/`.

## VS Code Preview

```bash
code --install-extension bernhard-42.ocp-cad-viewer
```

1. Select interpreter: `.venv`
2. Open viewer: `Ctrl+Shift+P` → "OCP CAD Viewer: Open Viewer"
3. Run script
