all: test

OPT :=
test:
	@clear
	@PYTHONPATH=. pytest --quiet $(OPT)

KEEP_FILES := Makefile
SUBMISSION_FILES := submission.py backup_submission.py
SCRIPT_FILES := script.py backup_script.py
EMPTY_FILES := 1 2 3 4
clean:
	@find . -maxdepth 1 -type f $(foreach f,$(KEEP_FILES), ! -name '$(f)') -exec rm {} +

	@for f in $(SUBMISSION_FILES); do cp template/submission.py $$f; done
	@for f in $(SCRIPT_FILES); do cp template/script.py $$f; done
	@touch $(EMPTY_FILES)

	@echo '🧹 Cleaned'

.PHONY: all test clean
