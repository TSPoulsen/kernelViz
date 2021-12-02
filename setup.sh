#!/usr/bin/bash

pip install -r requirements.txt
. scripts/getData.sh
python3 scripts/cleanData.py