MODULES=invoice
IGNORE=**/tests/*

all: pep8 flakes test

test:: run_tests report

analysis:: pep8 flakes

coveralls::
	coveralls

run_tests:
	@echo Running Tests...
	@nosetests --with-coverage --cover-package=orm_mothers tests/

report:
	@coverage report

pep8:
	@pep8 --statistics ${MODULES}

flakes:
	@pyflakes invoice
