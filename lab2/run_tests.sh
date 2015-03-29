#!/bin/bash

python -m unittest tests.sign
python -m unittest tests.functions_32bit
python -m unittest tests.functions_64bit
python -m unittest tests.cipher
