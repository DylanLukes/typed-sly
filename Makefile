PYTHON=python3
VENV=.venv

# Setup and install all of the required tools for building, testing, type checking,
# and deploying
setup::
	rm -rf $(VENV)
	$(PYTHON) -m venv $(VENV)
	./$(VENV)/bin/python -m pip install pyright
	./$(VENV)/bin/python -m pip install pytest
	./$(VENV)/bin/python -m pip install pytest-cov
	./$(VENV)/bin/python -m pip install build
	./$(VENV)/bin/python -m pip install twine

# Run type checking
typecheck::
	./$(VENV)/bin/python -m pyright

# Run unit tests
test::
	./$(VENV)/bin/python -m pip install .
	./$(VENV)/bin/python -m pytest --cov

# Build an artifact suitable for installing with pip
build::
	./$(VENV)/bin/python -m build
