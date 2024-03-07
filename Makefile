PYTHON_VERSION = 3.10.5
VENV := .venv
RUN := . $(VENV)/bin/activate;
_venv_init:
	@if [ ! -d "$(VENV)" ]; then\
		python -m venv $(VENV) --prompt=devTools;\
	fi
install:
	$(RUN) pip install -r requirements.txt
venv: _venv_init install