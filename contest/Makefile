all: test


OPT :=
test:
	@clear
	@PYTHONPATH=. pytest $(OPT)

uc = $(shell echo $(1) | tr a-z A-Z)
%:
	@clear
	@echo '[' "$(call uc,$@)".py ']'
	@PYTHONPATH=. poetry run pytest --quiet $(OPT) tests/test_$(call uc,$@).py


TEMPLATE_DIR := ../template
KEEP_FILES := Makefile __init__.py
SUBMISSION_FILES := {A,B,C,D,E,F,G}.py
SCRIPT_FILES := script.py
EMPTY_FILES := temp
clean:
	@find . -maxdepth 1 -type f $(foreach f,$(KEEP_FILES), ! -name '$(f)') -exec rm {} +

	@for f in $(SUBMISSION_FILES); do cp $(TEMPLATE_DIR)/template_submission.py $$f; done
	@for f in $(SCRIPT_FILES); do cp $(TEMPLATE_DIR)/template_script.py $$f; done
	@touch $(EMPTY_FILES)

	@echo 'Contest directory cleaned'


.PHONY: all test clean
