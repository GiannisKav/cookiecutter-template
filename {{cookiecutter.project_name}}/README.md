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

{%- if cookiecutter.ci_tool == "github_actions" %}
### Package Hosting with GitHub

This project uses GitHub to host the package. The GitHub Actions CI will create version tags which you can use to install the package directly from GitHub.

To install the package:

```bash
uv add "{{cookiecutter.project_name}} @ git+https://github.com/GiannisKav/{{cookiecutter.project_name}}.git"
```

You'll be prompted to enter your GitHub personal access token during installation.
{%- elif cookiecutter.ci_tool == "azure_pipelines" %}
### Package Hosting with Azure Artifacts

This project uses Azure Artifacts Feed to host the package. The Azure Pipelines CI will publish packages to your private feed.

To install the package directly:

```bash
uv pip install {{cookiecutter.project_name}} --index-url https://<ANY_NON_EMPTY_STRING>:<YOUR_PERSONAL_ACCESS_TOKEN>@{{cookiecutter.package_feed_url.split('https://')[-1]}}/simple/
```

#### Adding to your project

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
{%- endif %}

{%- if cookiecutter.ci_tool != "none" %}
## Package Releases

{%- if cookiecutter.ci_tool == "github_actions" %}
Releases are managed automatically by GitHub Actions. When changes are merged to the main branch, the pipeline will:

1. Create and push a new version tag
2. Make the package available for Git-based installation

The package can then be installed directly from GitHub using the command shown in the installation section.
{%- elif cookiecutter.ci_tool == "azure_pipelines" %}
Releases are managed automatically by Azure Pipelines. When changes are merged to the main branch, the pipeline will:

1. Create a new version tag
2. Build the package
3. Publish the package to your Azure Artifacts Feed

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
