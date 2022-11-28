#!/bin/bash
python3 -m venv venv
source venv/bin/activate
pip3 install flask
export FLASK_APP=fuzzcoin 
#export FLASK_ENV=development 
flask run --host=0.0.0.0 --port=8000

