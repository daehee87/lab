from flask import Blueprint, render_template, abort, session, Markup
from flask import redirect, url_for, request, flash, send_file
from datetime import datetime, timedelta
import uuid
import hashlib
import os, random
import string

dashboard = Blueprint("dashboard", __name__)

@dashboard.route("/readme")
def readme():
    return render_template("dashboard/readme.html")

@dashboard.route("/roadmap")
def roadmap():
    return render_template("dashboard/roadmap.html")

@dashboard.route("/")
def index():
    return render_template(
        "dashboard/index.html",
        n_cov="n_cov",
        n_crash="n_crash ",
        last_crash_project="last_crash_project",
        last_cov_project="last_cov_project",
        total_user="total_user",
        total_coin="total_coin",
        active_user="active_user",
        exec_sec="exec_sec",
        time="time",
        last_pofw="last_pofw",
        last_cov="last_cov",
        last_crash="last_crash",
        last_cheat="last_cheat",
        exec_sec_list=[],
        timestamp_list=[],
        high_cov="high_cov",
        high_cov2="high_cov2",
        high_crash="high_crash",
        high_crash2="high_crash2",
    )


@dashboard.route("/projects")
def projects_list():
    return render_template(
        "dashboard/projects-list.html",
        projects=None,
        stars=None,
        path=None,
        dates=None,
    )

@dashboard.route("/leaderboard")
def leaderboard():
    return render_template("dashboard/leaderboard.html", table=None)
