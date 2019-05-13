#!/bin/bash
# Runs all tests.
set -e
VENV=.env
[ -d $VENV ] && . $VENV/bin/activate
./pep8.sh
[ -d .tox ] && rm -Rf .tox || true
export TESTNAME=; tox
