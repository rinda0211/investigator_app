from flask import render_template, request, redirect, url_for

from sqlalchemy import and_
from sqlalchemy import or_

from investigator_app import app
from investigator_app import db
from investigator_app.models.investigator import Investigator
from investigator_app.models.investigator import Session

import ast, json, math

@app.route('/view/<int:id>', methods=['GET'])
def investigator_view(id):
    if request.method == 'GET':
        investigator = Investigator.query.get_or_404(id)
        skills = ast.literal_eval(investigator.skills)

        session_db = Session.query.all()
        sessions = []
        for session in session_db:
            PC_id = []
            if session.PC1_id: PC_id.append(int(session.PC1_id))
            if session.PC2_id: PC_id.append(int(session.PC2_id))
            if session.PC3_id: PC_id.append(int(session.PC3_id))
            if session.PC4_id: PC_id.append(int(session.PC4_id))
            if session.PC5_id: PC_id.append(int(session.PC5_id))
            if session.PC6_id: PC_id.append(int(session.PC6_id))
            if session.PC7_id: PC_id.append(int(session.PC7_id))
            if session.PC8_id: PC_id.append(int(session.PC8_id))
            if session.PC9_id: PC_id.append(int(session.PC9_id))
            if session.PC10_id: PC_id.append(int(session.PC10_id))
            if id in PC_id:
                sessions.append(session)
        return render_template('investigator/view_investigator.html', investigator = investigator, skills = skills, sessions = sessions)