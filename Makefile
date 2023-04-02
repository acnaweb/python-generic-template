install:
	echo conda activate template
	pip install -r requirements.txt

run:
	python src/app/app.py	

test:
	pytest