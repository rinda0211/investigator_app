from flask import render_template, request, redirect, url_for, jsonify

from sqlalchemy import and_
from sqlalchemy import or_

from investigator_app import app
from investigator_app import db
from investigator_app.models.investigator import Investigator

import ast, json, math, os, subprocess

@app.route('/copy_investigator/<int:id>', methods=['GET'])
def copy_investigator(id):
    if request.method == 'GET':

        ccfolia_text = '{"kind": "character", "data": {'
        
        investigator = Investigator.query.get_or_404(id)
        
        # 名前
        ccfolia_text = ccfolia_text + '"name": "' + investigator.name
        ccfolia_text = ccfolia_text + '(' + investigator.furigana + ')", '
        # イニシアティブ
        ccfolia_text = ccfolia_text + '"initiative": ' + str(investigator.DEX_sum) + ', '
        # いあきゃらリンク
        ccfolia_text = ccfolia_text + '"externalUrl": "' + investigator.iachara_link + '",'
        # 立ち絵リンク
        ccfolia_text = ccfolia_text + '"iconUrl": "' + investigator.img + '", '
        # 技能
        ccfolia_text = ccfolia_text + '"commands": "'
        # SANチェック
        ccfolia_text = ccfolia_text + '1d100<={SAN} 【正気度ロール】\\n'
        # アイデア
        ccfolia_text = ccfolia_text + '1d100<=' + str(investigator.ide_sum) + ' 【アイデア】\\n'
        # 幸運
        ccfolia_text = ccfolia_text + '1d100<=' + str(investigator.luck_sum) + ' 【幸運】\\n'
        # 知識
        ccfolia_text = ccfolia_text + '1d100<=' + str(investigator.knowledge_sum) + ' 【知識】\\n'
        # 技能
        skills_json = ast.literal_eval(investigator.skills)
        skills = []
        skills.extend(skills_json.get("battle_skills"))
        skills.extend(skills_json.get("search_skills"))
        skills.extend(skills_json.get("action_skills"))
        skills.extend(skills_json.get("interpersonal_skills"))
        skills.extend(skills_json.get("knowledge_skills"))

        # 三大探索技能を上に
        skills.sort(key=lambda skill: skill["name"] != "図書館")
        skills.sort(key=lambda skill: skill["name"] != "聞き耳")
        skills.sort(key=lambda skill: skill["name"] != "目星")

        # 全技能追加
        for skill in skills:
            points = skill.get("points")
            job_points = int(points.get("job_points"))
            interest_points = int(points.get("interest_points"))
            growth_points = int(points.get("growth_points"))
            others_points = int(points.get("others_points"))
            if job_points != 0 or interest_points != 0 or growth_points != 0 or others_points != 0:
                initial_points = int(points.get("initial_points"))
                sum_points = initial_points + job_points + interest_points + growth_points + others_points
                name = skill.get("name")
                ccfolia_text = ccfolia_text + 'CCB<=' + str(sum_points) + ' 【' + name + '】\\n'
        ccfolia_text = ccfolia_text + '", '

        # ステータス
        ccfolia_text = ccfolia_text + '"status": ['
        # HP
        ccfolia_text = ccfolia_text + '{"label": "HP", '
        ccfolia_text = ccfolia_text + '"value": ' + str(investigator.hp_sum) + ', '
        ccfolia_text = ccfolia_text + '"max": ' + str(investigator.hp_sum) + '}, '
        # MP
        ccfolia_text = ccfolia_text + '{"label": "MP", '
        ccfolia_text = ccfolia_text + '"value": ' + str(investigator.mp_sum) + ', '
        ccfolia_text = ccfolia_text + '"max": ' + str(investigator.mp_sum) + '}, '
        # SAN
        ccfolia_text = ccfolia_text + '{"label": "SAN", '
        ccfolia_text = ccfolia_text + '"value": ' + str(investigator.san_now) + ', '
        ccfolia_text = ccfolia_text + '"max": ' + str(investigator.san_now) + '}'
        ccfolia_text = ccfolia_text + '], '

        # パラメータ
        ccfolia_text = ccfolia_text + '"params": ['
        # STR
        ccfolia_text = ccfolia_text + '{"label": "STR", '
        ccfolia_text = ccfolia_text + '"value": "' + str(investigator.STR_sum) + '"}, '
        # CON
        ccfolia_text = ccfolia_text + '{"label": "CON", '
        ccfolia_text = ccfolia_text + '"value": "' + str(investigator.CON_sum) + '"}, '
        # POW
        ccfolia_text = ccfolia_text + '{"label": "POW", '
        ccfolia_text = ccfolia_text + '"value": "' + str(investigator.POW_sum) + '"}, '
        # DEX
        ccfolia_text = ccfolia_text + '{"label": "DEX", '
        ccfolia_text = ccfolia_text + '"value": "' + str(investigator.DEX_sum) + '"}, '
        # APP
        ccfolia_text = ccfolia_text + '{"label": "APP", '
        ccfolia_text = ccfolia_text + '"value": "' + str(investigator.APP_sum) + '"}, '
        # SIZ
        ccfolia_text = ccfolia_text + '{"label": "SIZ", '
        ccfolia_text = ccfolia_text + '"value": "' + str(investigator.SIZ_sum) + '"}, '
        # INT
        ccfolia_text = ccfolia_text + '{"label": "INT", '
        ccfolia_text = ccfolia_text + '"value": "' + str(investigator.INT_sum) + '"}, '
        # EDU
        ccfolia_text = ccfolia_text + '{"label": "EDU", '
        ccfolia_text = ccfolia_text + '"value": "' + str(investigator.EDU_sum) + '"} '
        ccfolia_text = ccfolia_text + ']'


        ccfolia_text = ccfolia_text + ''

        ccfolia_text = ccfolia_text + "}}"
        
        return ccfolia_text