# fuzzcoin-web

This folder contains the Flask-based fuzzcoin website. Structure is based on
the [official flask tutorial](https://github.com/pallets/flask/tree/master/examples/tutorial).

## Installation

A virtualenv is highly recommended to keep fuzzcoin-web's dependencies isolated
from your system.

### Linux:

```shell
$ python3 -m venv venv
$ . venv/bin/activate
```

### Windows:

```shell
$ py -3 -m venv venv
$ venv\Scripts\activate.bat
```

And then finally install fuzzcoin-web's dependencies using:

```shell
$ pip install -e .
```

## Running

```shell
$ export FLASK_APP=fuzzcoin
$ export FLASK_ENV=development
$ flask run
```

This should start up a development serving on Open http://127.0.0.1:5000

## Testing

```shell
$ pip install -e ".[test]"
$ pytest
```

## Formatting

Use [black](https://github.com/psf/black) for formatting the code:

```shell
$ pip install black
$ black tests/ fuzzcoin/
```
