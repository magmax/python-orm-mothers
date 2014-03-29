MODULES=orm_mothers
IGNORE=**/tests/*

all: pep8 flakes test

test:: run_tests

analysis:: pep8 flakes

coveralls::
	coveralls

run_tests:
	@echo Running Tests...
	@nosetests --with-coverage --cover-package=${MODULES} tests/

pep8:
	@pep8 --statistics ${MODULES}

flakes:
	@pyflakes invoice
