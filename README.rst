Usage
-----

Put the csv to here as `input.csv`

.. code:: sh

    pipenv run 'python csv2parquet/__init__.py'

Installation
------------

.. code:: sh

    pipenv install git+ssh://github.com/yongjhih/csv2parquet.git#egg=csv2parquet


.. code:: sh

    pipenv install


Development
-----------

.. code:: sh

    pipenv install
    pipenv install -d
    pipenv run "pytest"
    pipenv run "mypy --ignore-missing-imports flo"

Coverage
-----------

.. code:: sh

    pipenv run 'pytest tests --cov=flo'

Stack
-----

- Data Classes - PEP 557 (Python 3.7)
- Type hints - PEP 3107 (Python 3.0), PEP 484 (Python 3.5), PEP 526 (Python 3.6), PEP 563 (Python 3.7)
- Type checking - mypy (Python 3.6)
- Literal String Interpolation - PEP 498 (Python 3.6)
