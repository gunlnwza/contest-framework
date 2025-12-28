all:

uc = $(shell echo $(1) | tr a-z A-Z)
%:
	@clear
	@echo '[' $(call uc,$@) ']'
	@PYTHONPATH=. poetry run pytest --quiet tests/test_$(call uc,$@).py

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

re:

.PHONY: all clean fclean re
