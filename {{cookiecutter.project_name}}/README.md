# {{cookiecutter.project_name}}

{{cookiecutter.project_description}}

## Getting started with your project

First, create a repository on GitHub with the same name as this project, and then run the following commands:

```bash
git clone git@github.com:GiannisKav/{{cookiecutter.project_name}}
cd {{cookiecutter.project_name}}
```

Finally, install the environment and the pre-commit hooks with

```bash
make install
```
{%- if cookiecutter.is_package == "y" %}

## Installing the package

### Using uv directly

```bash
uv pip install {{cookiecutter.project_name}} --index-url https://<ANY_NON_EMPTY_STRING>:<YOUR_PERSONAL_ACCESS_TOKEN>@{{cookiecutter.package_feed_url.split('https://')[-1]}}/simple/
```

### Adding to your project

Add to your pyproject.toml:

```toml
[tool.uv.sources]
{{cookiecutter.project_slug}} = { index = "internal" }

[[tool.uv.index]]
name = "internal"
url = "https://{{cookiecutter.package_feed_url.split('https://')[-1]}}/simple/"
explicit = true
```

And set the following environment variables:

```bash
export UV_INDEX_INTERNAL_PASSWORD=<YOUR_PERSONAL_ACCESS_TOKEN>
export UV_INDEX_INTERNAL_USERNAME=<ANY_NON_EMPTY_STRING>
```
{%- if cookiecutter.ci_tool != "none" %}

## Package Releases

Releases are managed automatically by the CI pipeline. When changes are merged to the main branch, the pipeline will create a new version tag and publish the package.
{%- if cookiecutter.ci_tool == "github_actions" %}

### CI Setup - GitHub Actions

You need to add a repository secret for package publishing:

1. Go to your repository on GitHub
2. Navigate to Settings > Secrets and variables > Actions
3. Click "New repository secret"
4. Name: `UV_PUBLISH_TOKEN`
5. Value: Your package repository access token
6. Click "Add secret"
{%- endif %}
{%- if cookiecutter.ci_tool == "azure_pipelines" %}

### CI Setup - Azure Pipelines

You need to create a variable group for package publishing:

1. In your Azure DevOps project, go to Pipelines > Library
2. Create a new variable group named "publish-tokens"
3. Add a variable:
   - Name: `UV_PUBLISH_TOKEN`
   - Value: Your package repository access token
4. Save the variable group
5. Make sure the pipeline has access to this variable group
{%- endif %}
{%- endif %}
{%- endif %}
{%- if cookiecutter.dockerfile == "y" %}

## Docker

To build the docker image, run:

```bash
make build-image
```

To run the docker container, run:

```bash
make run-container
```
{%- endif %}

---

Repository initiated with [cookiecutter-template](https://github.com/GiannisKav/cookiecutter-template).
