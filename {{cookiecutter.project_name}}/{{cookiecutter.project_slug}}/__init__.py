{% if cookiecutter.is_package == "y" -%}
"""{{cookiecutter.project_name}} package."""

try:
    # Try to get version from package metadata (when installed)
    from importlib.metadata import version

    __version__ = version("{{cookiecutter.project_name}}")
except Exception:
    # During development or when not installed
    __version__ = "0.0.0.dev0"
{%- endif %}
