"""{{ cookiecutter.package_name }} - {{ cookiecutter.package_description }}"""

__author__ = '{{ cookiecutter.author_name }} <{{ cookiecutter.author_email }}>'
__all__ = []

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
