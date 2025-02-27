PYTHON_VERSION := {{cookiecutter.python_version}}

.PHONY: install
install: ## Install the virtual environment and install the pre-commit hooks
	@echo "🚀 Installing python $(PYTHON_VERSION)"
	@uv python install $(PYTHON_VERSION)
	@uv python pin $(PYTHON_VERSION)
	@echo "🚀 Creating virtual environment using uv"
	@uv sync
	@uv run pre-commit install
	@uv export --locked --no-dev --format requirements-txt > requirements.txt
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
	@uv run pre-commit run -a

.PHONY: test
test: ## Test the code with pytest
	@echo "🚀 Testing code: Running pytest"
	@uv run pytest
{% if cookiecutter.is_package == "y" %}

.PHONY: clean
clean: ## Remove build artifacts
	@echo "🚀 Cleaning build artifacts"
	@rm -rf build dist *.egg-info

.PHONY: release
release: check clean ## Release a new version
	@echo "🚀 Starting release process"
	echo "🚀 Current version: v$$(uv run hatch version)"; \
	read -p "Enter version segment to bump (patch/minor/major): " segment; \
	uv run hatch version $$segment; \
	NEW_VERSION=$$(uv run hatch version); \
	echo "🚀 Updated to version: v$$NEW_VERSION"; \
	uv lock --upgrade-package {{cookiecutter.project_name}}; \
	uv build; \
	echo "🚀 Package built"; \
	read -p "Enter commit message: " msg; \
	git add -A; \
	git commit -m "v$$NEW_VERSION: $$msg"; \
	git tag -f "v$$NEW_VERSION"; \
	echo "🚀 Tagged commit with version v$$NEW_VERSION"; \
	git push origin main --tags; \
	echo "🚀 Pushed changes and tags"; \
	uv publish; \
	echo "🚀 Published package"; \
	echo "🚀 Release of version v$$NEW_VERSION completed successfully!"
{% endif %}

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help
