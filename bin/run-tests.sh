#!/bin/bash

set -e
RET=0

pip uninstall -y $(basename $PWD) || echo "Could not uninstall."
pip install -U "git+file://$PWD" --no-cache-dir --process-dependency-links

mv powerlibs x
export $(cat test.env)
PYTHONPATH=. pytest -vvv tests/ || RET=$?
mv x powerlibs

exit $RET
