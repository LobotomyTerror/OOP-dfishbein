TEST = python -m pytest
TEST_ARGS = -s --verbose --color=yes
TYPE_CHECK = mypy --strict --allow-untyped-decorators --ignore-missing-imports
STYLE_CHECK = flake8
COV = pytest

.PHONY: all
all: check-style check-type run-test pytest_cov clean

.PHONY: check-type
check-type:
	$(TYPE_CHECK) assignments/A3-unittesting/morsecodepalindromes
	$(TYPE_CHECK) assignments/A4-Mocking_Hypothesis/titlecost
	$(TYPE_CHECK) assignments/A5-API
	
.PHONY: check-style
check-style:
	$(STYLE_CHECK) assignments/

# discover and run all tests
.PHONY: run-test
run-test:
	$(TEST) $(TEST_ARGS) assignments/A3-unittesting/morsecodepalindromes/tests
	$(TEST) $(TEST_ARGS) assignments/A4-Mocking_Hypothesis/titlecost/tests

.PHONY: pytest_cov
pytest_cov:
	$(TEST) -v --cov-report=html:./assignments/A3-unittesting/morsecodepalindromes/coverage_report --cov-report=term --cov=./assignments/A3-unittesting/morsecodepalindromes/ ./assignments/A3-unittesting/morsecodepalindromes/tests
	$(TEST) -v --cov-report=html:./assignments/A4-Mocking_Hypothesis/titlecost/coverage_report --cov-report=term --cov=./assignments/A4-Mocking_Hypothesis/titlecost/ ./assignments/A4-Mocking_Hypothesis/titlecost/tests

.PHONY: clean
clean:
	# remove all caches recursively
	rm -rf `find . -type d -name __pycache__` # remove all pycache
	rm -rf `find . -type d -name .pytest_cache` # remove all pytest cache
	rm -rf `find . -type d -name .mypy_cache` # remove all mypy cache
	rm -rf `find . -type d -name .hypothesis` # remove all hypothesis cache
	rm -rf `find . -type d -name .coverage` # remove all coverage cache 
	