.PHONY: test
test:
	python -m pytest tests -s -v -o log_cli=true -o log_cli_level=DEBUG

.PHONY: style
style:
	isort . && ruff format ./