from flask import render_template, request, redirect, url_for

from sqlalchemy import and_
from sqlalchemy import or_

from investigator_app import app
from investigator_app import db
from investigator_app.models.investigator import Investigator

import ast, json, math

@app.route('/list', methods=['GET'])
def investigator_list():
    if request.method == 'GET':
        investigators = Investigator.query.all()
        return render_template('investigator/investigator_list.html', investigators=investigators)