test:
	@clear
	@PYTHONPATH=. pytest

OPT := --quiet
A B C D E F G:
	@clear
	@echo '[ $@ ]'
	@PYTHONPATH=. pytest $(OPT) tests/test_$@.py

a b c d e f g:
	@clear
	@upper=$(shell echo $@ | tr a-z A-Z); \
	echo "[ $$upper ]"; \
	PYTHONPATH=. pytest $(OPT) tests/test_$$upper.py

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

fclean: clean

.PHONY: test, A, B, C, D, E, F, G, clean, fclean
