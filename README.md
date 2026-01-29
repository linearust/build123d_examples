# build123d Examples

## Usage

```bash
uv run --with build123d python base_plate.py
```

Exports to `exports/`.

## Live Preview (VS Code)

1. Install extension
   ```bash
   code --install-extension bernhard-42.ocp-cad-viewer
   ```

2. Open viewer: `Ctrl+Shift+P` → "OCP CAD Viewer: Open Viewer"

3. Run with viewer support
   ```bash
   uv run --with build123d --with ocp-vscode python base_plate.py
   ```
