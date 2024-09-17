# Cookiecutter Project Template

This is a Cookiecutter template that can be used to initiate a Python project with a basic structure and some useful tools. It includes:

- [uv](https://docs.astral.sh/uv/) for dependency management
- Pre-commit hooks with [pre-commit](https://pre-commit.com/)
- Code quality with:
  - [ruff](https://github.com/charliermarsh/ruff)
  - [mypy](https://mypy.readthedocs.io/en/stable/)
  - [prettier](https://prettier.io/)
  - [deptry](https://github.com/fpgmaas/deptry/)
- Testing and coverage with [pytest](https://docs.pytest.org/en/7.1.x/) and [codecov](https://about.codecov.io/)
- Compatibility testing for multiple versions of Python with [Tox](https://tox.wiki/en/latest/) #TODO
- Containerization with [Docker](https://www.docker.com/)

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

To enable the code coverage reports, see [here](https://fpgmaas.github.io/cookiecutter-poetry/features/codecov/).

## Acknowledgements

This project is partially based on Florian Maas\'s [cookiecutter-poetry](https://github.com/fpgmaas/cookiecutter-poetry) repository.
