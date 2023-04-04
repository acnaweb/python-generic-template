dev:
	pip install -r requirements.dev.txt

install: dev 
	pip install -r requirements.txt

run:
	python app/cli.py	

test:
	pytest

