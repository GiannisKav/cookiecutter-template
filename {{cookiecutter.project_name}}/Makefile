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
release: install check clean ## Create a new release
	@echo "🚀 Running release"

	@# Get current version from the latest tag
	@LATEST_TAG=$$(git tag --sort=-v:refname | head -1 2>/dev/null || echo "v0.0.0"); \
	CURRENT_VERSION=$$(echo $$LATEST_TAG | sed 's/^v//'); \
	MAJOR=$$(echo $$CURRENT_VERSION | cut -d. -f1); \
	MINOR=$$(echo $$CURRENT_VERSION | cut -d. -f2); \
	PATCH=$$(echo $$CURRENT_VERSION | cut -d. -f3); \
	NEW_MINOR=$$((MINOR + 1)); \
	NEW_VERSION="$$MAJOR.$$NEW_MINOR.0"; \
	NEW_TAG="v$$NEW_VERSION"; \
	COMMIT_TAG=$$(git tag --points-at HEAD); \
	if [ -n "$$COMMIT_TAG" ]; then \
		echo "This commit is already tagged with $$COMMIT_TAG - skipping release"; \
		exit 0; \
	fi; \
	git tag -a "$$NEW_TAG" -m "Release $$NEW_VERSION"; \
	git push origin "$$NEW_TAG"; \
	git checkout "$$NEW_TAG"; \
	uv build; \
	echo "Publishing version $$NEW_VERSION"; \
	uv publish
{% endif %}

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help
