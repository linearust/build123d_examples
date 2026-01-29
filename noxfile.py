import nox

nox.options.default_venv_backend = "uv"


@nox.session(python="3.12")
def run(session):
    session.install("build123d")
    session.run("python", session.posargs[0] if session.posargs else "base_plate.py")
