MODULES=orm_mothers
IGNORE=**/tests/*

all: pep8 flakes test

test:: run_tests

xcoverage:: run_tests_xcoverage

analysis:: pep8 flakes

coveralls::
	coveralls

run_tests:
	@echo Running Tests...
	@nosetests --with-coverage --cover-package=${MODULES} tests/

run_tests_xcoverage:
	@echo Running Tests...
	@nosetests --with-xcoverage tests/

pep8:
	@pep8 --statistics ${MODULES}

flakes:
	@pyflakes ${MODULES}
