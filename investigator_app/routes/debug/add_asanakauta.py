from flask import render_template, request, redirect, url_for

from sqlalchemy import and_
from sqlalchemy import or_

from investigator_app import app
from investigator_app import db
from investigator_app.models.investigator import Investigator

import ast, json, math

# 変数
from investigator_app.data.skills_default import skills_default
from investigator_app.data.debug.skills_asanakauta import skills_asanakauta

@app.route('/add_asanaka', methods=['GET'])
def add_asanaka():
    if request.method == 'GET':
        # 技能
        skills = str(skills_asanakauta)

        # 名前
        form_name = "浅中詩"
        form_furigana = "あさなかうた"

        # PL
        form_player = "リンダ"

        # 立ち絵
        form_img = "https://lh3.googleusercontent.com/d/1e3iAk9wc_-IvndC9HeEyUfA3901s7jXy"

        # 基本情報
        form_job = "探偵"
        form_age = 18
        form_sex = "女"
        form_height = "160"
        form_weight = "56"
        # form_birthplace = request.form.get('birthplace')
        # form_hair_color = request.form.get('hair_color')
        # form_eye_color = request.form.get('eye_color')
        # form_skin_color = request.form.get('skin_color')

        # ステータス基本
        form_STR = 7
        form_CON = 7
        form_POW = 11
        form_DEX = 11
        form_APP = 17
        form_SIZ = 11
        form_INT = 18
        form_EDU = 14

        # ステータス増加分
        form_STR_add = 0
        form_CON_add = 0
        form_POW_add = 0
        form_DEX_add = 0
        form_APP_add = 1
        form_SIZ_add = 0
        form_INT_add = 0
        form_EDU_add = 0

        # ステータス一時的
        form_STR_tmp = 0
        form_CON_tmp = 0
        form_POW_tmp = 0
        form_DEX_tmp = 0
        form_APP_tmp = 0
        form_SIZ_tmp = 0
        form_INT_tmp = 0
        form_EDU_tmp = 0

        # ステータス合計
        form_STR_sum = form_STR + form_STR_add + form_STR_tmp
        form_CON_sum = form_CON + form_CON_add + form_CON_tmp
        form_POW_sum = form_POW + form_POW_add + form_POW_tmp
        form_DEX_sum = form_DEX + form_DEX_add + form_DEX_tmp
        form_APP_sum = form_APP + form_APP_add + form_APP_tmp
        form_SIZ_sum = form_SIZ + form_SIZ_add + form_SIZ_tmp
        form_INT_sum = form_INT + form_INT_add + form_INT_tmp
        form_EDU_sum = form_EDU + form_EDU_add + form_EDU_tmp
        
        # ステータス計算
        form_hp = math.ceil((form_CON_sum + form_SIZ_sum)/2)
        form_mp = form_POW_sum
        form_san = form_POW_sum * 5
        form_ide = form_INT_sum * 5
        form_luck = form_POW_sum * 5
        form_knowledge = form_EDU_sum * 5
        form_hp_add = 0
        form_mp_add = 0
        form_san_add = 0
        form_ide_add = 0
        form_luck_add = 0
        form_knowledge_add = 0
        form_hp_tmp = 0
        form_mp_tmp = 0
        form_san_tmp = 0
        form_ide_tmp = 0
        form_luck_tmp = 0
        form_knowledge_tmp = 0
        form_hp_sum = form_hp + form_hp_add + form_hp_tmp
        form_mp_sum = form_mp + form_mp_add + form_mp_tmp
        form_san_sum = form_san + form_san_add + form_san_tmp
        form_ide_sum = form_ide + form_ide_add + form_ide_tmp
        form_luck_sum = form_luck + form_luck_add + form_luck_tmp
        form_knowledge_sum = form_knowledge + form_knowledge_add + form_knowledge_tmp

        form_damage_bonus = "+0"
        form_san_now = 46

        investigator = Investigator(
            name = form_name,
            furigana = form_furigana,
            Player = form_player,
            img = form_img,
            job = form_job,
            age = form_age,
            sex = form_sex,
            height = form_height,
            weight = form_weight,
            STR = form_STR,
            CON = form_CON,
            POW = form_POW,
            DEX = form_DEX,
            APP = form_APP,
            SIZ = form_SIZ,
            INT = form_INT,
            EDU = form_EDU,
            STR_add = form_STR_add,
            CON_add = form_CON_add,
            POW_add = form_POW_add,
            DEX_add = form_DEX_add,
            APP_add = form_APP_add,
            SIZ_add = form_SIZ_add,
            INT_add = form_INT_add,
            EDU_add = form_EDU_add,
            STR_tmp = form_STR_tmp,
            CON_tmp = form_CON_tmp,
            POW_tmp = form_POW_tmp,
            DEX_tmp = form_DEX_tmp,
            APP_tmp = form_APP_tmp,
            SIZ_tmp = form_SIZ_tmp,
            INT_tmp = form_INT_tmp,
            EDU_tmp = form_EDU_tmp,
            STR_sum = form_STR_sum,
            CON_sum = form_CON_sum,
            POW_sum = form_POW_sum,
            DEX_sum = form_DEX_sum,
            APP_sum = form_APP_sum,
            SIZ_sum = form_SIZ_sum,
            INT_sum = form_INT_sum,
            EDU_sum = form_EDU_sum,
            hp = form_hp,
            mp = form_mp,
            san = form_san,
            ide = form_ide,
            luck = form_luck,
            knowledge = form_knowledge,
            hp_add = form_hp_add,
            mp_add = form_mp_add,
            san_add = form_san_add,
            ide_add = form_ide_add,
            luck_add = form_luck_add,
            knowledge_add = form_knowledge_add,
            hp_tmp = form_hp_tmp,
            mp_tmp = form_mp_tmp,
            san_tmp = form_san_tmp,
            ide_tmp = form_ide_tmp,
            luck_tmp = form_luck_tmp,
            knowledge_tmp = form_knowledge_tmp,
            hp_sum = form_hp_sum,
            mp_sum = form_mp_sum,
            san_sum = form_san_sum,
            ide_sum = form_ide_sum,
            luck_sum = form_luck_sum,
            knowledge_sum = form_knowledge_sum,
            damage_bonus = form_damage_bonus,
            san_now = form_san_now,
            skills = skills
        )
        db.session.add(investigator)
        db.session.commit()
        return redirect(url_for('index'))
   