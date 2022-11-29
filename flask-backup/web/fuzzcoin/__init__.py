import os, hashlib, datetime
from flask import Flask, render_template, session, abort
from flask import Response, redirect, url_for, request
from fuzzcoin.dashboard import dashboard

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.register_blueprint(dashboard)
    return app
