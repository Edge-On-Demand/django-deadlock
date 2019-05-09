#!/bin/bash
set -e

VENV=.env

# Remove existing virtualenv if it exists.
[ -d $VENV ] && rm -Rf $VENV

virtualenv -p python3 $VENV
. $VENV/bin/activate
pip install -U pip

pip install -r requirements-test.txt
