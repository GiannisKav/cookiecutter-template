# syntax=docker/dockerfile:1

FROM python:3.11-slim-buster

ENV POETRY_VERSION=1.7.1 \
    POETRY_VIRTUALENVS_CREATE=false

# Install build essentials and libpq-dev for psycopg2
RUN apt-get update && \
    apt-get install -y libpq-dev gcc && \
    rm -rf /var/lib/apt/lists/*

# Install poetry
RUN pip install "poetry==$POETRY_VERSION"

# Copy only requirements to cache them in docker layer
WORKDIR /code
COPY poetry.lock pyproject.toml /code/

# Project initialization:
RUN poetry install --no-interaction --no-ansi --no-root --without dev

# Copy Python code to the Docker image
COPY {{cookiecutter.project_slug}} /code/{{cookiecutter.project_slug}}/

CMD [ "python", "{{cookiecutter.project_slug}}/foo.py"]
