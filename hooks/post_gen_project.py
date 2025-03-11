#!/usr/bin/env python
import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath: str) -> None:
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def remove_dir(filepath: str) -> None:
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, filepath))


def create_dir(dirpath: str) -> None:
    os.makedirs(os.path.join(PROJECT_DIRECTORY, dirpath), exist_ok=True)


if __name__ == "__main__":
    if "{{cookiecutter.dockerfile}}" != "y":
        remove_file("Dockerfile")
        remove_file("docker-compose.yml")

    if "{{cookiecutter.codecov}}" != "y":
        remove_file("codecov.yaml")

    if "{{cookiecutter.devcontainer}}" != "y":
        remove_dir(".devcontainer")

    # Handle CI tool options
    ci_tool = "{{cookiecutter.ci_tool}}"
    if ci_tool == "none":
        # Remove both CI configurations
        if os.path.exists(os.path.join(PROJECT_DIRECTORY, "azure-pipelines.yml")):
            remove_file("azure-pipelines.yml")
        if os.path.exists(os.path.join(PROJECT_DIRECTORY, ".github/workflows/publish.yml")):
            remove_file(".github/workflows/publish.yml")
            # Try to remove parent directories if empty
            try:
                os.rmdir(os.path.join(PROJECT_DIRECTORY, ".github/workflows"))
                os.rmdir(os.path.join(PROJECT_DIRECTORY, ".github"))
            except OSError:  # Directory not empty or doesn't exist
                pass
    elif ci_tool == "azure_pipelines":
        # Remove GitHub Actions
        if os.path.exists(os.path.join(PROJECT_DIRECTORY, ".github/workflows/publish.yml")):
            remove_file(".github/workflows/publish.yml")
            # Try to remove parent directories if empty
            try:
                os.rmdir(os.path.join(PROJECT_DIRECTORY, ".github/workflows"))
                os.rmdir(os.path.join(PROJECT_DIRECTORY, ".github"))
            except OSError:  # Directory not empty or doesn't exist
                pass
    elif ci_tool == "github_actions":
        # Remove Azure Pipelines
        if os.path.exists(os.path.join(PROJECT_DIRECTORY, "azure-pipelines.yml")):
            remove_file("azure-pipelines.yml")
