.PHONY: install
install: ## Install the poetry environment and install the pre-commit hooks
	@echo "🚀 Creating virtual environment using pyenv and poetry"
	@poetry lock --no-update
	@poetry export -f requirements.txt --output requirements.txt
	@poetry install --sync
	@poetry run pre-commit install
	@poetry shell
{%- if cookiecutter.dockerfile == "y"%}

.PHONY: build-image
build-image: ## Build the docker image
	@echo "🚀 Building docker image"
		@@docker-compose build main_app

.PHONY: run-container
run-container: ## Run the docker container
	@echo "🚀 Running docker container"
	@docker run -d {{cookiecutter.project_name}}
{%- endif %}

.PHONY: check
check: ## Run code quality tools.
	@echo "🚀 Checking code quality: Running pre-commit"
	@poetry run pre-commit run -a

.PHONY: test
test: ## Test the code with pytest
	@echo "🚀 Testing code: Running pytest"
{%- if cookiecutter.codecov == "y"%}
	@poetry run pytest --cov={{cookiecutter.project_slug}} --cov-config=pyproject.toml --cov-report=html
{%- else %}
	@poetry run pytest --doctest-modules
{%- endif %}

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help
