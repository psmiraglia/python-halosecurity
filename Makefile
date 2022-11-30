default: install

install:
	pip install -e .

flake8:
	flake8 setup.py halosecurity/*.py halosecurity/base/*.py

isort-diff:
	isort --diff setup.py halosecurity/*.py halosecurity/base/*.py

isort:
	isort setup.py halosecurity/*.py halosecurity/base/*.py

style: flake8 isort-diff
