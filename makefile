install:
	cd src && \
	pip install -e . && \
	cd ..

test: 
	pytest -vv -s  &&\
	mypy .

format:
	isort . && \
	black -l 79 .
