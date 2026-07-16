from flask import render_template, request, redirect, url_for

from sqlalchemy import and_
from sqlalchemy import or_

from investigator_app import app
from investigator_app import db
from investigator_app.models.investigator import Investigator
from investigator_app.models.investigator import Session

import ast, json, math

@app.route('/delete_session/<int:id>', methods=['POST'])
def delete_session(id):
    if request.method == 'POST':
        session = Session.query.get(id)
        db.session.delete(session)
        db.session.commit()
        return redirect(url_for('session_list'))