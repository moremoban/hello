pip freeze
nosetests --with-cov --cover-package hello_cli --cover-package tests --with-doctest --doctest-extension=.rst README.rst tests docs/source hello_cli && flake8 . --exclude=.moban.d --builtins=unicode,xrange,long
