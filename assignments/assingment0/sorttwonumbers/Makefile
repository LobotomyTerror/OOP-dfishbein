PROGRAM = python3
MAIN = a_zero.py
TEST = test_a_zero.py

all: localtest unittest typecheck stylecheck clean

localtest:
	@cat 1.in | ${PROGRAM} ${MAIN} | diff - 1.ans
	@cat 2.in | ${PROGRAM} ${MAIN} | diff - 2.ans
	@cat 3.in | ${PROGRAM} ${MAIN} | diff - 3.ans
	@echo "Local tests have passed moving to unitesting..."

unittest:
	@pytest ${TEST}

typecheck:
	@mypy --strict ${MAIN} ${TEST}

stylecheck:
	@flake8 ${MAIN} ${TEST}

clean:
	@rm -rf .pytest_cache
	@rm -rf .mypy_cache
	@rm -rf __pycache__
