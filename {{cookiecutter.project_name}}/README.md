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
{%- endif %}---

Repository initiated with [cookiecutter-template](https://github.com/GiannisKav/cookiecutter-template).
