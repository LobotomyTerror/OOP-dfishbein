TEST = python -m pytest
TEST_ARGS = -s -v --color=yes --code-highlight=yes 
TYPE_TEST = mypy --strict --show-error-code-links --pretty --allow-untyped-decorators
STYLE_TEST = flake8
FIX_STYLE = autopep8 -v -aa -r --in-place
COV_ARGS = --cov=. --cov=/tests --cov-report=html:coverage_report

.PHONY: all
all: auto_fix check_type check_style run_tests clean

.PHONY: auto_fix
auto_fix:
	$(FIX_STYLE) .

.PHONY: check_type
check_type:
	$(TYPE_TEST) .

.PHONY: check_style
check_style:
	$(STYLE_TEST) .

.PHONY: run_tests
run_tests:
	$(TEST) $(TEST_ARGS) .

.PHONY: pytest_cov
pytest_cov:
	$(TEST) $(COV_ARGS)

.PHONY: clean
clean:
	@rm -rf `find . -type d -name __pycache__`
	@rm -rf `find . -type d -name .pytest_cache`
	@rm -rf `find . -type d -name .mypy_cache`
	@rm -rf `find . -type d -name .hypothesis`
	@rm -rf `find . -type d -name .coverage`