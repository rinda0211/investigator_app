from flask import render_template, request, redirect, url_for, jsonify

from sqlalchemy import and_
from sqlalchemy import or_

from investigator_app import app
from investigator_app import db
from investigator_app.models.investigator import Investigator
from investigator_app.models.investigator import Session

import ast, json, math

# 変数
from investigator_app.data.skills_default import skills_default

@app.route('/load_session', methods=['GET', 'POST'])
def load_session():
    if request.method == 'GET':
        return render_template('session/load_session.html')
    if request.method == 'POST':

        file = request.files["json_file"]

        session_json = json.load(file)

        session = Session(
            senario_name = session_json.get("senario_name"),
            date1 = session_json.get("date1"),
            date2 = session_json.get("date2"),
            date3 = session_json.get("date3"),
            date4 = session_json.get("date4"),
            date5 = session_json.get("date5"),
            date6 = session_json.get("date6"),
            date7 = session_json.get("date7"),
            date8 = session_json.get("date8"),
            date9 = session_json.get("date9"),
            date10 = session_json.get("date10"),
            KP = session_json.get("KP"),
            KPC = session_json.get("KPC"),
            KPC_id = session_json.get("KPC_id"),
            SKP1 = session_json.get("SKP1"),
            SKPC1 = session_json.get("SKPC1"),
            SKPC1_id = session_json.get("SKPC1_id"),
            SKP2 = session_json.get("SKP2"),
            SKPC2 = session_json.get("SKPC2"),
            SKPC2_id = session_json.get("SKPC2_id"),
            SKP3 = session_json.get("SKP3"),
            SKPC3 = session_json.get("SKPC3"),
            SKPC3_id = session_json.get("SKPC3_id"),
            PL1 = session_json.get("PL1"),
            PC1 = session_json.get("PC1"),
            PC1_id = session_json.get("PC1_id"),
            PL2 = session_json.get("PL2"),
            PC2 = session_json.get("PC2"),
            PC2_id = session_json.get("PC2_id"),
            PL3 = session_json.get("PL3"),
            PC3 = session_json.get("PC3"),
            PC3_id = session_json.get("PC3_id"),
            PL4 = session_json.get("PL4"),
            PC4 = session_json.get("PC4"),
            PC4_id = session_json.get("PC4_id"),
            PL5 = session_json.get("PL5"),
            PC5 = session_json.get("PC5"),
            PC5_id = session_json.get("PC5_id"),
            PL6 = session_json.get("PL6"),
            PC6 = session_json.get("PC6"),
            PC6_id = session_json.get("PC6_id"),
            PL7 = session_json.get("PL7"),
            PC7 = session_json.get("PC7"),
            PC7_id = session_json.get("PC7_id"),
            PL8 = session_json.get("PL8"),
            PC8 = session_json.get("PC8"),
            PC8_id = session_json.get("PC8_id"),
            PL9 = session_json.get("PL9"),
            PC9 = session_json.get("PC9"),
            PC9_id = session_json.get("PC9_id"),
            PL10 = session_json.get("PL10"),
            PC10 = session_json.get("PC10"),
            PC10_id = session_json.get("PC10_id")
        )
        db.session.add(session)
        db.session.commit()

        return jsonify({
            "status": "ok"
        })