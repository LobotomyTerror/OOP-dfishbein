TEST = python -m pytest
TEST_ARGS = -s -v --color=yes --code-highlight=yes 
TYPE_TEST = mypy --strict --show-error-code-links --pretty --allow-untyped-decorators
STYLE_TEST = flake8
FIX_STYLE = autopep8 -v -aa -r --in-place
PROG = python
MAIN = convexpolygonarea.py

.PHONY: all
all: auto_fix check_type check_style run_tests test_input clean

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

.PHONY: clean
clean:
	@rm -rf __pycache__
	@rm -rf .pytest_cache
	@rm -rf .mypy_cache

.PHONY: test_input
test_input:
	@cat data/1.in | $(PROG) $(MAIN) | diff - data/1.ans
	@cat data/2.in | $(PROG) $(MAIN) | diff - data/2.ans
	@cat data/3.in | $(PROG) $(MAIN) | diff - data/3.ans
	@echo "Local tests of main program have passed all tests"
