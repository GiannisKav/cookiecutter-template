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

{% if cookiecutter.is_package == "y" -%}
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

## Publishing the package

To publish a new version of the package:

```bash
export UV_PUBLISH_TOKEN=<YOUR_PERSONAL_ACCESS_TOKEN>
make release
```

{%- endif %}
{% if cookiecutter.dockerfile == "y" -%}
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
