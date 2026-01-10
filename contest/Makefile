all: test

OPT :=
test:
	@clear
	@PYTHONPATH=. pytest --quiet $(OPT)

KEEP_FILES := Makefile template.py
EMPTY_FILES := submission.py temp.py 1 2 3 4
clean:
	@find . -maxdepth 1 -type f $(foreach f,$(KEEP_FILES), ! -name '$(f)') -exec rm {} +
	@touch $(EMPTY_FILES)
	@cp template.py submission.py
	@echo '🧹 Cleaned'

.PHONY: all test clean
