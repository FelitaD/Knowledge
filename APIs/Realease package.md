---
tags: 
- tech/data_engineering/projects
- doc
aliases:
publish: true
sr-due: 2022-10-27
sr-interval: 15
sr-ease: 270
---
# How to create a new release

1. Modify toml file : increase package's version
2. Upgrade build
`pip3 install --upgrade build`
3. Build the wheel : produces 2 files, a .whl and a .tar.gz
`python -m build`
4. Install from the wheel : select the last file version 
`pip3 install dist/.. --force-reinstall`
5. Upload to pypi : username \_\_token\_\_ 
`python3 -m twine upload dist/*`
6. Reinstall package in Airflow


****
[Doc setup tools](https://setuptools.pypa.io/en/latest/userguide/quickstart.html)
https://packaging.python.org/en/latest/tutorials/packaging-projects/

