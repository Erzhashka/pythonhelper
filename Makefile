.PHONY: install run debug clean lint lint-strict help

help:
	@echo "Available targets:"
	@echo "  make install      - Install project dependencies"
	@echo "  make run          - Run the maze generator"
	@echo "  make debug        - Run in debug mode"
	@echo "  make clean        - Clean temporary files and caches"
	@echo "  make lint         - Run flake8 and mypy linters"
	@echo "  make lint-strict  - Run mypy in strict mode"

install:
	pip install flake8 mypy

run:
	python3 a_maze_ing.py config.txt

debug:
	python3 -m pdb a_maze_ing.py config.txt

clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .mypy_cache -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	rm -f maze.txt

lint:
	flake8 . --max-line-length=88
	mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

lint-strict:
	flake8 . --max-line-length=88
	mypy . --strict
