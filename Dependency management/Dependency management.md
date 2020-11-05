# Dependency management with PIP:

Easily install your dependencies with pip. Pipenv is a dependency manager for Python projects.

Pin your requirements with a requirements.txt file. pip install -r requirements.txt and all the project's dependencies will be installed automatically! Placing this file into version control alongside the source code makes it easy for others to use and edit it. In order to ensure complete reproducibility, your requirements.txt file should include all of your projectâ€™s transitive (indirect) dependencies, not just your direct dependencies.

```sh
pip install "SomePackage"
```
Or for a specific package version:
```sh
pip install "SomePackage == 1.0"
```
