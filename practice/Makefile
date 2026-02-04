all: test

OPT :=
test:
	@clear
	@PYTHONPATH=. pytest --quiet $(OPT)

TEMPLATE_DIR := ../template
KEEP_FILES := Makefile __init__.py
SUBMISSION_FILES := submission.py
SCRIPT_FILES := script.py
EMPTY_FILES := temp
clean:
	@find . -maxdepth 1 -type f $(foreach f,$(KEEP_FILES), ! -name '$(f)') -exec rm {} +

	@for f in $(SUBMISSION_FILES); do cp $(TEMPLATE_DIR)/template_submission.py $$f; done
	@for f in $(SCRIPT_FILES); do cp $(TEMPLATE_DIR)/template_script.py $$f; done
	@touch $(EMPTY_FILES)

	@echo 'Practice directory cleaned'

.PHONY: all test clean
