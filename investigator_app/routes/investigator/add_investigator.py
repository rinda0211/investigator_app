from flask import render_template, request, redirect, url_for

from sqlalchemy import and_
from sqlalchemy import or_

from investigator_app import app
from investigator_app import db
from investigator_app.models.investigator import Investigator

import ast, json, math

# 変数
from investigator_app.data.skills_default import skills_default

@app.route('/add_investigator', methods=['GET', 'POST'])
def add_investigator():
    if request.method == 'GET':
        return render_template('investigator/add_investigator.html', skills=skills_default)
    if request.method == 'POST':
        # 技能
        skills = ""
        # 戦闘系技能
        form_battle_skills = request.form.get('battle_skills_json')
        skills = skills + "{\"battle_skills\": " + form_battle_skills
        # 探索系技能
        form_search_skills = request.form.get('search_skills_json')
        skills = skills + ", \"search_skills\": " + form_search_skills
        # 行動系技能
        form_action_skills = request.form.get('action_skills_json')
        skills = skills + ", \"action_skills\": " + form_action_skills
        # 交渉系技能
        form_interpersonal_skills = request.form.get('interpersonal_skills_json')
        skills = skills + ", \"interpersonal_skills\": " + form_interpersonal_skills
        # 知識系技能
        form_knowledge_skills = request.form.get('knowledge_skills_json')
        skills = skills + ", \"knowledge_skills\": " + form_knowledge_skills
        # 変数まとめ
        skills = skills + "}"

        # 通過セッション
        form_sessions = request.form.get('session_list')
        print(form_sessions)

        # 名前
        form_name = request.form.get('name')
        form_furigana = request.form.get('furigana')

        # ロスト
        form_lost = request.form.get('lost') != None

        # PL
        form_player = request.form.get('player')

        # 基本情報
        form_job = request.form.get('job')
        form_age = request.form.get('age')
        form_sex = request.form.get('sex')
        form_height = request.form.get('height')
        form_weight = request.form.get('weight')
        form_birthplace = request.form.get('birthplace')
        form_hair_color = request.form.get('hair_color')
        form_eye_color = request.form.get('eye_color')
        form_skin_color = request.form.get('skin_color')

        # 画像
        form_img = request.form.get('img', default=None)
        if(form_img[8:13] == "drive"):
            form_img = form_img[29:]
            form_img_length = len(form_img)
            cut_point = 0
            for i in range(3, form_img_length):
                if form_img[i] == '/':
                    cut_point = i
                    break
            form_img = "https://lh3.googleusercontent.com" + form_img[:cut_point]
        # リンク
        form_imgs_link = request.form.get('imgs_link')
        form_iachara_link = request.form.get('iachara_link')

        # ステータス基本
        form_STR = request.form.get('STR', default=0, type=int)
        form_CON = request.form.get('CON', default=0, type=int)
        form_POW = request.form.get('POW', default=0, type=int)
        form_DEX = request.form.get('DEX', default=0, type=int)
        form_APP = request.form.get('APP', default=0, type=int)
        form_SIZ = request.form.get('SIZ', default=0, type=int)
        form_INT = request.form.get('INT', default=0, type=int)
        form_EDU = request.form.get('EDU', default=0, type=int)

        # ステータス増加分
        form_STR_add = request.form.get('STR_add', default=0, type=int)
        form_CON_add = request.form.get('CON_add', default=0, type=int)
        form_POW_add = request.form.get('POW_add', default=0, type=int)
        form_DEX_add = request.form.get('DEX_add', default=0, type=int)
        form_APP_add = request.form.get('APP_add', default=0, type=int)
        form_SIZ_add = request.form.get('SIZ_add', default=0, type=int)
        form_INT_add = request.form.get('INT_add', default=0, type=int)
        form_EDU_add = request.form.get('EDU_add', default=0, type=int)

        # ステータス一時的
        form_STR_tmp = request.form.get('STR_tmp', default=0, type=int)
        form_CON_tmp = request.form.get('CON_tmp', default=0, type=int)
        form_POW_tmp = request.form.get('POW_tmp', default=0, type=int)
        form_DEX_tmp = request.form.get('DEX_tmp', default=0, type=int)
        form_APP_tmp = request.form.get('APP_tmp', default=0, type=int)
        form_SIZ_tmp = request.form.get('SIZ_tmp', default=0, type=int)
        form_INT_tmp = request.form.get('INT_tmp', default=0, type=int)
        form_EDU_tmp = request.form.get('EDU_tmp', default=0, type=int)

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
        form_hp_add = request.form.get('hp_add', default=0, type=int)
        form_mp_add = request.form.get('mp_add', default=0, type=int)
        form_san_add = request.form.get('san_add', default=0, type=int)
        form_ide_add = request.form.get('ide_add', default=0, type=int)
        form_luck_add = request.form.get('luck_add', default=0, type=int)
        form_knowledge_add = request.form.get('knowledge_add', default=0, type=int)
        form_hp_tmp = request.form.get('hp_tmp', default=0, type=int)
        form_mp_tmp = request.form.get('mp_tmp', default=0, type=int)
        form_san_tmp = request.form.get('san_tmp', default=0, type=int)
        form_ide_tmp = request.form.get('ide_tmp', default=0, type=int)
        form_luck_tmp = request.form.get('luck_tmp', default=0, type=int)
        form_knowledge_tmp = request.form.get('knowledge_tmp', default=0, type=int)
        form_hp_sum = form_hp + form_hp_add + form_hp_tmp
        form_mp_sum = form_mp + form_mp_add + form_mp_tmp
        form_san_sum = form_san + form_san_add + form_san_tmp
        form_ide_sum = form_ide + form_ide_add + form_ide_tmp
        form_luck_sum = form_luck + form_luck_add + form_luck_tmp
        form_knowledge_sum = form_knowledge + form_knowledge_add + form_knowledge_tmp

        damage_bonus = form_STR_sum + form_SIZ_sum
        if damage_bonus <= 12: form_damage_bonus = "-1D6"
        elif damage_bonus <= 16: form_damage_bonus = "-1D4"
        elif damage_bonus <= 24: form_damage_bonus = "+0"
        elif damage_bonus <= 32: form_damage_bonus = "+1D4"
        elif damage_bonus <= 40: form_damage_bonus = "+1D6"
        elif damage_bonus <= 46: form_damage_bonus = "+2D6"
        else:
            damage = math.ceil((damage_bonus - 45) / 16) + 2
            form_damage_bonus = "+" + str(damage) + "D6"

        form_san_now = request.form.get('san_now', default=0, type=int)

        investigator = Investigator(
            name = form_name,
            furigana = form_furigana,
            lost = form_lost,
            Player = form_player,
            job = form_job,
            age = form_age,
            sex = form_sex,
            height = form_height,
            weight = form_weight,
            birthplace = form_birthplace,
            hair_color = form_hair_color,
            eye_color = form_eye_color,
            skin_color = form_skin_color,
            img = form_img,
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
            skills = skills,
            sessions = form_sessions,
            imgs_link = form_imgs_link,
            iachara_link = form_iachara_link,
        )
        db.session.add(investigator)
        db.session.commit()
        return redirect(url_for('index'))
   