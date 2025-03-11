# Cookiecutter Project Template

This is a Cookiecutter template that can be used to initiate a Python project with a basic structure and some useful tools. It includes:

- [uv](https://docs.astral.sh/uv/) for dependency management
- Pre-commit hooks with [pre-commit](https://pre-commit.com/)
- Code quality with:
  - [ruff](https://github.com/charliermarsh/ruff)
  - [mypy](https://mypy.readthedocs.io/en/stable/)
  - [prettier](https://prettier.io/)
  - [deptry](https://github.com/fpgmaas/deptry/)
- Testing with [pytest](https://docs.pytest.org/en/stable/)
- Coverage tracking with [codecov](https://about.codecov.io/)
- CI/CD with Azure Pipelines or GitHub Actions (optional)
- Containerization with Docker (optional)

## Quickstart

On your local machine, install cookiecutter, navigate to the directory in which you want to
create a project directory, and run the following command:

```bash
uvx cookiecutter https://github.com/GiannisKav/cookiecutter-template.git
```

or if you don't have `uv` installed yet:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.cargo/env
uv tool install cookiecutter
uvx cookiecutter https://github.com/GiannisKav/cookiecutter-template.git
```

Finally, install the environment and the pre-commit hooks with

```bash
make install
```

## Acknowledgements

This project is partially based on Florian Maas\'s [cookiecutter-poetry](https://github.com/fpgmaas/cookiecutter-poetry) repository.
