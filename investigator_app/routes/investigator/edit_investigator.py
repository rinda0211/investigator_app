from flask import render_template, request, redirect, url_for

from sqlalchemy import and_
from sqlalchemy import or_

from investigator_app import app
from investigator_app import db
from investigator_app.models.investigator import Investigator

import ast, json, math

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def investigator_edit(id):
    if request.method == 'GET':
        investigator = Investigator.query.get_or_404(id)
        skills = ast.literal_eval(investigator.skills)
        if(investigator.sessions): sessions = ast.literal_eval(investigator.sessions)
        else: sessions = []
        return render_template('investigator/edit_investigator.html', investigator = investigator, skills = skills, sessions = sessions)
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

        # 更新
        investigator = Investigator.query.get(id)
        # 各カラム
        investigator.name = form_name
        investigator.furigana = form_furigana
        investigator.Player = form_player
        investigator.job = form_job
        investigator.age = form_age
        investigator.sex = form_sex
        investigator.height = form_height
        investigator.weight = form_weight
        investigator.birthplace = form_birthplace
        investigator.hair_color = form_hair_color
        investigator.eye_color = form_eye_color
        investigator.skin_color = form_skin_color
        investigator.img = form_img
        investigator.STR = form_STR
        investigator.CON = form_CON
        investigator.POW = form_POW
        investigator.DEX = form_DEX
        investigator.APP = form_APP
        investigator.SIZ = form_SIZ
        investigator.INT = form_INT
        investigator.EDU = form_EDU
        investigator.STR_add = form_STR_add
        investigator.CON_add = form_CON_add
        investigator.POW_add = form_POW_add
        investigator.DEX_add = form_DEX_add
        investigator.APP_add = form_APP_add
        investigator.SIZ_add = form_SIZ_add
        investigator.INT_add = form_INT_add
        investigator.EDU_add = form_EDU_add
        investigator.STR_tmp = form_STR_tmp
        investigator.CON_tmp = form_CON_tmp
        investigator.POW_tmp = form_POW_tmp
        investigator.DEX_tmp = form_DEX_tmp
        investigator.APP_tmp = form_APP_tmp
        investigator.SIZ_tmp = form_SIZ_tmp
        investigator.INT_tmp = form_INT_tmp
        investigator.EDU_tmp = form_EDU_tmp
        investigator.STR_sum = form_STR_sum
        investigator.CON_sum = form_CON_sum
        investigator.POW_sum = form_POW_sum
        investigator.DEX_sum = form_DEX_sum
        investigator.APP_sum = form_APP_sum
        investigator.SIZ_sum = form_SIZ_sum
        investigator.INT_sum = form_INT_sum
        investigator.EDU_sum = form_EDU_sum
        investigator.hp = form_hp
        investigator.mp = form_mp
        investigator.san = form_san
        investigator.ide = form_ide
        investigator.luck = form_luck
        investigator.knowledge = form_knowledge
        investigator.hp_add = form_hp_add
        investigator.mp_add = form_mp_add
        investigator.san_add = form_san_add
        investigator.ide_add = form_ide_add
        investigator.luck_add = form_luck_add
        investigator.knowledge_add = form_knowledge_add
        investigator.hp_tmp = form_hp_tmp
        investigator.mp_tmp = form_mp_tmp
        investigator.san_tmp = form_san_tmp
        investigator.ide_tmp = form_ide_tmp
        investigator.luck_tmp = form_luck_tmp
        investigator.knowledge_tmp = form_knowledge_tmp
        investigator.hp_sum = form_hp_sum
        investigator.mp_sum = form_mp_sum
        investigator.san_sum = form_san_sum
        investigator.ide_sum = form_ide_sum
        investigator.luck_sum = form_luck_sum
        investigator.knowledge_sum = form_knowledge_sum
        investigator.damage_bonus = form_damage_bonus
        investigator.san_now = form_san_now
        investigator.skills = skills
        investigator.sessions = form_sessions
        investigator.lost = form_lost
        investigator.imgs_link = form_imgs_link
        investigator.iachara_link = form_iachara_link

        db.session.merge(investigator)
        db.session.commit()
        
        return redirect(url_for('investigator_list'))