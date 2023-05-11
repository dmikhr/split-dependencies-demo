freeze:
	pip freeze > requirements.txt
	python -m split_dependencies

