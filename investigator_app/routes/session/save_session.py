from flask import render_template, request, redirect, url_for, jsonify

from sqlalchemy import and_
from sqlalchemy import or_

from investigator_app import app
from investigator_app import db
from investigator_app.models.investigator import Investigator
from investigator_app.models.investigator import Session

import ast, json, math, os

@app.route('/save_session/<int:id>', methods=['GET'])
def save_session(id):
    if request.method == 'GET':
        session = Session.query.get_or_404(id)
        session_dict = {
            "senario_name": session.senario_name,
            "date1": session.date1,
            "date2": session.date2,
            "date3": session.date3,
            "date4": session.date4,
            "date5": session.date5,
            "date6": session.date6,
            "date7": session.date7,
            "date8": session.date8,
            "date9": session.date9,
            "date10": session.date10,
            "KP": session.KP,
            "KPC": session.KPC,
            "KPC_id": session.KPC_id,
            "SKP1": session.SKP1,
            "SKPC1": session.SKPC1,
            "SKPC1_id": session.SKPC1_id,
            "SKP2": session.SKP2,
            "SKPC2": session.SKPC2,
            "SKPC2_id": session.SKPC2_id,
            "SKP3": session.SKP3,
            "SKPC3": session.SKPC3,
            "SKPC3_id": session.SKPC3_id,
            "PL1": session.PL1,
            "PC1": session.PC1,
            "PC1_id": session.PC1_id,
            "PL2": session.PL2,
            "PC2": session.PC2,
            "PC2_id": session.PC2_id,
            "PL3": session.PL3,
            "PC3": session.PC3,
            "PC3_id": session.PC3_id,
            "PL4": session.PL4,
            "PC4": session.PC4,
            "PC4_id": session.PC4_id,
            "PL5": session.PL5,
            "PC5": session.PC5,
            "PC5_id": session.PC5_id,
            "PL6": session.PL6,
            "PC6": session.PC6,
            "PC6_id": session.PC6_id,
            "PL7": session.PL7,
            "PC7": session.PC7,
            "PC7_id": session.PC7_id,
            "PL8": session.PL8,
            "PC8": session.PC8,
            "PC8_id": session.PC8_id,
            "PL9": session.PL9,
            "PC9": session.PC9,
            "PC9_id": session.PC9_id,
            "PL10": session.PL10,
            "PC10": session.PC10,
            "PC10_id": session.PC10_id
        }

        file_name = "json/session/" + str(session.id) + "." + session.senario_name + ".json"

        with open(file_name, "w", encoding="utf-8") as f:
            json.dump(session_dict, f, ensure_ascii=False, indent=4)
        
        return jsonify({
            "status": "ok"
        })