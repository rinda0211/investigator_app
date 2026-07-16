from flask import render_template, request, redirect, url_for

from sqlalchemy import and_
from sqlalchemy import or_

from investigator_app import app
from investigator_app import db
from investigator_app.models.investigator import Investigator
from investigator_app.models.investigator import Session

import ast, datetime, json, math

@app.route('/session_list', methods=['GET', 'POST'])
def session_list():
    if request.method == 'GET':
        sessions = Session.query.all()
        return render_template('session/session_list.html', sessions=sessions)