.PHONY: setup run run-debug

setup:
	docker-compose up -d
	python3 -m venv venv
	source ./venv/bin/activate
	pip install -r requirements.txt

run: setup
	source ./venv/bin/activate
	flask --app run.py run

run-debug: setup
	source ./venv/bin/activate
	flask --app run.py run --debug