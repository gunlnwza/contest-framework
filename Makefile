test:
	@clear
	@PYTHONPATH=. pytest

A B C D E F G:
	@clear
	@echo '[ $@ ]'
	@PYTHONPATH=. pytest -q tests/test_$@.py

a b c d e f g:
	@clear
	@upper=$(shell echo $@ | tr a-z A-Z); \
	echo "[ $$upper ]"; \
	PYTHONPATH=. pytest -q tests/test_$$upper.py

clean:
	cat template.py > A.py
	cat template.py > B.py
	cat template.py > C.py
	cat template.py > D.py
	cat template.py > E.py
	cat template.py > F.py
	cat template.py > G.py
	> 1
	> 2
	> 3
	> 4

.PHONY: test, A, B, C, D, E, F, G, clean
