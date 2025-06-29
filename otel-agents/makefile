.PHONY: all venv install run clean

VENV_DIR := .venv
PYTHON := $(VENV_DIR)/bin/python
PIP := $(VENV_DIR)/bin/pip

all: run

# Create a virtual environment
venv:
	@echo "Creating virtual environment in $(VENV_DIR)..."
	python3 -m venv $(VENV_DIR)
	@echo "Virtual environment created."

# Install requirements into the virtual environment
install: venv
	@echo "Installing requirements from requirements.txt..."
	$(PIP) install -r requirements.txt
	@echo "Requirements installed."

# Clean up generated files and the virtual environment
clean:
	@echo "Cleaning up..."
	@rm -rf $(VENV_DIR)
	@rm -f report.txt
	@echo "Clean up complete."

