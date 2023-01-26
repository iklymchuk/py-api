# This is a template project for API test automation

## Dummy swagger API for coverage: https://petstore.swagger.io

## Note on Codespaces Virtualenv 
Checkout how if you run `pip freeze | wc -l` there are many packages we may not want
Try `which python`
1. `virtualenv ~/.venv` 
2. Always source this virt env:
`vim ~/.bashrc` and put in `source ~/.venv/bin/activate`
3. Verify the right python `which python` and try `pip freeze | wc -l` it should be 0

## Make file
* `make install` install the project dependencies
* `make test` perform tests execution and coverage stat
* `make format` formatting the code
* `make all` perform all operations 

## Pytest execution
* Library style: `python -m pytest -vv -s`
* Run tests by keyword expressions: `python -m pytest -vv -k "user"`
* Run a specific test within a modele: `python -m pytest testing/test_user.py::test_random_user`
* Run tests by marker expressions: `https://docs.pytest.org/en/7.2.x/how-to/usage.html#usage`
* Profile tests: `python -m pytest -vv --durations=10 --durations-min=1.0`
* Distributed testing `https://pypi.org/project/pytest-xdist/`