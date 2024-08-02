install:
	poetry install


brain-games:
	poetry run brain-games


build:
	poetry build


publish:
	poetry publish --dry-run


package-install:
	python3 -m pip install --user dist/*.whl


lint:
	poetry run flake8 brain_games


reinstall:
	python3 -m pip install  --force-reinstall dist/*.whl

test-coverage:
	poetry run pytest --cov=brain_games --cov-report xml
