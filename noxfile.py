import nox

nox.options.default_venv_backend = "uv"

DEPS = ["build123d", "ocp-vscode"]


@nox.session(python="3.12")
def run(session):
    """Run a build123d script. Usage: nox -s run -- [script.py]"""
    session.install(*DEPS)
    script = session.posargs[0] if session.posargs else "base_plate.py"
    session.run("python", script)


@nox.session(python="3.12")
def export(session):
    """Export all models to exports/."""
    import glob

    session.install(*DEPS)
    scripts = [s for s in glob.glob("*.py") if s != "noxfile.py"]
    for script in scripts:
        session.run("python", script)
