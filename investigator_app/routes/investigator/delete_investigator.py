from flask import render_template, request, redirect, url_for

from sqlalchemy import and_
from sqlalchemy import or_

from investigator_app import app
from investigator_app import db
from investigator_app.models.investigator import Investigator

import ast, json, math

@app.route('/delete_investigator/<int:id>', methods=['POST'])
def delete_investigator(id):
    if request.method == 'POST':
        investigator = Investigator.query.get(id)
        db.session.delete(investigator)
        db.session.commit()
        return redirect(url_for('investigator_list'))