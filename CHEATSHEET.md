Cheatsheet
==========
This is my first PyPI package, so I need some guidelines for myself.

Build and install localy
------------------------
```
  python3 -m unittest discover
  python3 -m build
  pip3 install dist/<package-and-version>.whl --force-reinstall
```
This is not good, it is not recommended to execute `setup.py`, but idk how to
run tests properly. Do I have to use `tox` for that?

Publish new version
-------------------
Before publishing make sure that tests are completed and version in setup is
up-to-date.
```
  python3 -m unittest discover
  python3 -m build
  python3 -m twine upload --skip-existing dist/*
```
After that add a tag to release commit at the package github page.
