.PHONY: test setup clean

# Default target
.DEFAULT_GOAL := help

# Help command
help:
	@echo "Lab Makefile"
	@echo ""
	@echo "Usage:"
	@echo "  make test         Run all tests"
	@echo "  make lint         Run all linters"
	@echo "  make clean        Clean cache files"
	@echo "  make setup        Setup development environment"


# Setup development environment
setup: clean
	$(MAKE) -C ./task_1 setup

# Run all tests
test:
	$(MAKE) -C ./task_1 test

# Run formatting and type checking
lint:
	$(MAKE) -C ./task_1 lint

# Clean cache files
clean:
	$(MAKE) -C ./task_1 clean