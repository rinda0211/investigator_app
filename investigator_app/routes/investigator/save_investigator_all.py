from flask import render_template, request, redirect, url_for, jsonify

from sqlalchemy import and_
from sqlalchemy import or_

from investigator_app import app
from investigator_app import db
from investigator_app.models.investigator import Investigator

import ast, json, math, os

@app.route('/save_investigator_all', methods=['GET'])
def save_investigator_all():
    if request.method == 'GET':
        investigators = Investigator.query.all()
        for investigator in investigators:
            investigator_dict = {
                "name": investigator.name,
                "furigana": investigator.furigana,
                "Player": investigator.Player,
                "img": investigator.img,
                "job": investigator.job,
                "age": investigator.age,
                "sex": investigator.sex,
                "height": investigator.height,
                "weight": investigator.weight,
                "birthplace": investigator.birthplace,
                "hair_color": investigator.hair_color,
                "eye_color": investigator.eye_color,
                "skin_color": investigator.skin_color,
                "STR": investigator.STR,
                "CON": investigator.CON,
                "POW": investigator.POW,
                "DEX": investigator.DEX,
                "APP": investigator.APP,
                "SIZ": investigator.SIZ,
                "INT": investigator.INT,
                "EDU": investigator.EDU,
                "STR_add": investigator.STR_add,
                "CON_add": investigator.CON_add,
                "POW_add": investigator.POW_add,
                "DEX_add": investigator.DEX_add,
                "APP_add": investigator.APP_add,
                "SIZ_add": investigator.SIZ_add,
                "INT_add": investigator.INT_add,
                "EDU_add": investigator.EDU_add,
                "STR_tmp": investigator.STR_tmp,
                "CON_tmp": investigator.CON_tmp,
                "POW_tmp": investigator.POW_tmp,
                "DEX_tmp": investigator.DEX_tmp,
                "APP_tmp": investigator.APP_tmp,
                "SIZ_tmp": investigator.SIZ_tmp,
                "INT_tmp": investigator.INT_tmp,
                "EDU_tmp": investigator.EDU_tmp,
                "STR_sum": investigator.STR_sum,
                "CON_sum": investigator.CON_sum,
                "POW_sum": investigator.POW_sum,
                "DEX_sum": investigator.DEX_sum,
                "APP_sum": investigator.APP_sum,
                "SIZ_sum": investigator.SIZ_sum,
                "INT_sum": investigator.INT_sum,
                "EDU_sum": investigator.EDU_sum,
                "hp": investigator.hp,
                "mp": investigator.mp,
                "san": investigator.san,
                "ide": investigator.ide,
                "luck": investigator.luck,
                "knowledge": investigator.knowledge,
                "hp_add": investigator.hp_add,
                "mp_add": investigator.mp_add,
                "san_add": investigator.san_add,
                "ide_add": investigator.ide_add,
                "luck_add": investigator.luck_add,
                "knowledge_add": investigator.knowledge_add,
                "hp_tmp": investigator.hp_tmp,
                "mp_tmp": investigator.mp_tmp,
                "san_tmp": investigator.san_tmp,
                "ide_tmp": investigator.ide_tmp,
                "luck_tmp": investigator.luck_tmp,
                "knowledge_tmp": investigator.knowledge_tmp,
                "hp_sum": investigator.hp_sum,
                "mp_sum": investigator.mp_sum,
                "san_sum": investigator.san_sum,
                "ide_sum": investigator.ide_sum,
                "luck_sum": investigator.luck_sum,
                "knowledge_sum": investigator.knowledge_sum,
                "damage_bonus": investigator.damage_bonus,
                "san_now": investigator.san_now,
                "damage_bonus": investigator.damage_bonus,
                "skills": investigator.skills,
                "sessions": investigator.sessions,
                "memo": investigator.memo,
                "lost": investigator.lost
            }

            file_name = "json/investigator/" + str(investigator.id) + "." + investigator.name + ".json"

            with open(file_name, "w", encoding="utf-8") as f:
                json.dump(investigator_dict, f, ensure_ascii=False, indent=4)
        
        return jsonify({
            "status": "ok"
        })