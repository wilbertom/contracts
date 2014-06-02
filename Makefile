#make all:
#	/bin/env python tests.py

make tests:
	/usr/bin/env python -m unittest discover contratos.test_contracts
	/usr/bin/env python -m unittest discover contratos.test_extras

make install:
	/usr/bin/env python setup.py install

