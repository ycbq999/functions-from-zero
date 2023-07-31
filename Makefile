install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=main --cov=calCLI --cov=mylib test_*.py

format:	
	black *.py mylib/*.py

lint:
	pylint --disable=R,C --extension-pkg-whitelist='pydantic' --ignore-patterns=test_.*?py *.py mylib/*.py

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

refactor: format lint

deploy:
	aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin 158095287634.dkr.ecr.us-east-2.amazonaws.com
	docker build -t logistics .
	docker tag logistics:latest 158095287634.dkr.ecr.us-east-2.amazonaws.com/logistics:latest
	docker push 158095287634.dkr.ecr.us-east-2.amazonaws.com/logistics:latest
	
all: install lint test format deploy