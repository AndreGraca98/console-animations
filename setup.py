from setuptools import find_packages, setup

from _version import __version__

setup(
    name="animations",
    version=__version__,
    author="André Graça",
    author_email="andrepgraca+github_animations@gmail.com",
    description=open("README.md").read(255),
    long_description=open("README.md").read(),
    platforms="Python",
    packages=find_packages(),
)
