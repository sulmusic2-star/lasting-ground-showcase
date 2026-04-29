PYTHON ?= python3

.PHONY: test coverage ci

test:
	$(PYTHON) -m pytest -q

coverage:
	$(PYTHON) -m coverage run -m pytest
	$(PYTHON) -m coverage report
	$(PYTHON) -m coverage json -o coverage/coverage.json

ci: test coverage
