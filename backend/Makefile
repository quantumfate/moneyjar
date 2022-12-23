freeze:
	pip freeze --exclude-editable | grep -v "pkg-resources" > requirements.txt
install:
	pip install -r requirements.txt
source:
	source venv/bin/activate
venv:
	python -m venv venv
