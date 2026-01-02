.PHONY: help install init seed run test clean

help:
	@echo "Student Management System - Available Commands"
	@echo "=============================================="
	@echo "make install    - Install dependencies"
	@echo "make init       - Initialize database"
	@echo "make seed       - Seed sample data"
	@echo "make run        - Run development server"
	@echo "make test       - Run tests"
	@echo "make clean      - Clean up generated files"

install:
	pip install -r requirements.txt

init:
	python scripts/init_db.py

seed:
	python scripts/seed_data.py

run:
	python run.py

test:
	pytest

clean:
	rm -rf __pycache__ */__pycache__ */*/__pycache__
	rm -rf .pytest_cache
	rm -rf htmlcov
	rm -rf .coverage
	rm -rf *.egg-info
	rm -rf dist build