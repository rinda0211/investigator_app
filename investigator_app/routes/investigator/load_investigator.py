from flask import render_template, request, redirect, url_for, jsonify

from sqlalchemy import and_
from sqlalchemy import or_

from investigator_app import app
from investigator_app import db
from investigator_app.models.investigator import Investigator

import ast, json, math

# 変数
from investigator_app.data.skills_default import skills_default

@app.route('/load_investigator', methods=['GET', 'POST'])
def load_investigator():
    if request.method == 'GET':
        return render_template('investigator/load_investigator.html')
    if request.method == 'POST':

        file = request.files["json_file"]

        investigator_json = json.load(file)

        investigator = Investigator(
            name = investigator_json.get("name"),
            furigana = investigator_json.get("furigana"),
            Player = investigator_json.get("Player"),
            img = investigator_json.get("img"),
            job = investigator_json.get("job"),
            age = investigator_json.get("age"),
            sex = investigator_json.get("sex"),
            height = investigator_json.get("height"),
            weight = investigator_json.get("weight"),
            birthplace = investigator_json.get("birthplace"),
            hair_color = investigator_json.get("hair_color"),
            eye_color = investigator_json.get("eye_color"),
            skin_color = investigator_json.get("skin_color"),
            STR = investigator_json.get("STR"),
            CON = investigator_json.get("CON"),
            POW = investigator_json.get("POW"),
            DEX = investigator_json.get("DEX"),
            APP = investigator_json.get("APP"),
            SIZ = investigator_json.get("SIZ"),
            INT = investigator_json.get("INT"),
            EDU = investigator_json.get("EDU"),
            STR_add = investigator_json.get("STR_add"),
            CON_add = investigator_json.get("CON_add"),
            POW_add = investigator_json.get("POW_add"),
            DEX_add = investigator_json.get("DEX_add"),
            APP_add = investigator_json.get("APP_add"),
            SIZ_add = investigator_json.get("SIZ_add"),
            INT_add = investigator_json.get("INT_add"),
            EDU_add = investigator_json.get("EDU_add"),
            STR_tmp = investigator_json.get("STR_tmp"),
            CON_tmp = investigator_json.get("CON_tmp"),
            POW_tmp = investigator_json.get("POW_tmp"),
            DEX_tmp = investigator_json.get("DEX_tmp"),
            APP_tmp = investigator_json.get("APP_tmp"),
            SIZ_tmp = investigator_json.get("SIZ_tmp"),
            INT_tmp = investigator_json.get("INT_tmp"),
            EDU_tmp = investigator_json.get("EDU_tmp"),
            STR_sum = investigator_json.get("STR_sum"),
            CON_sum = investigator_json.get("CON_sum"),
            POW_sum = investigator_json.get("POW_sum"),
            DEX_sum = investigator_json.get("DEX_sum"),
            APP_sum = investigator_json.get("APP_sum"),
            SIZ_sum = investigator_json.get("SIZ_sum"),
            INT_sum = investigator_json.get("INT_sum"),
            EDU_sum = investigator_json.get("EDU_sum"),
            hp = investigator_json.get("hp"),
            mp = investigator_json.get("mp"),
            san = investigator_json.get("san"),
            ide = investigator_json.get("ide"),
            luck = investigator_json.get("luck"),
            knowledge = investigator_json.get("knowledge"),
            hp_add = investigator_json.get("hp_add"),
            mp_add = investigator_json.get("mp_add"),
            san_add = investigator_json.get("san_add"),
            ide_add = investigator_json.get("ide_add"),
            luck_add = investigator_json.get("luck_add"),
            knowledge_add = investigator_json.get("knowledge_add"),
            hp_tmp = investigator_json.get("hp_tmp"),
            mp_tmp = investigator_json.get("mp_tmp"),
            san_tmp = investigator_json.get("san_tmp"),
            ide_tmp = investigator_json.get("ide_tmp"),
            luck_tmp = investigator_json.get("luck_tmp"),
            knowledge_tmp = investigator_json.get("knowledge_tmp"),
            hp_sum = investigator_json.get("hp_sum"),
            mp_sum = investigator_json.get("mp_sum"),
            san_sum = investigator_json.get("san_sum"),
            ide_sum = investigator_json.get("ide_sum"),
            luck_sum = investigator_json.get("luck_sum"),
            knowledge_sum = investigator_json.get("knowledge_sum"),
            damage_bonus = investigator_json.get("damage_bonus"),
            san_now = investigator_json.get("san_now"),
            skills = investigator_json.get("skills"),
            sessions = investigator_json.get("sessions"),
            memo = investigator_json.get("memo"),
            lost = investigator_json.get("lost"),
            iachara_link = investigator_json.get("iachara_link"),
            imgs_link = investigator_json.get("imgs_link")
        )
        db.session.add(investigator)
        db.session.commit()

        return jsonify({
            "status": "ok"
        })