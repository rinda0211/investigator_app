from flask import render_template, request, redirect, url_for

from sqlalchemy import and_
from sqlalchemy import or_

from investigator_app import app
from investigator_app import db
from investigator_app.models.investigator import Investigator

import ast, json, math

@app.route('/search', methods=['GET', 'POST'])
def search_investigator():
    if request.method == 'GET':
        return render_template('investigator/search_investigator.html')
    if request.method == 'POST':
        # 基本情報
        form_name = request.form.get('name')
        form_Player = request.form.get('Player')
        form_age = request.form.get('age')
        form_age_option = request.form.get('age_option')
        form_sex = request.form.get('sex')
        # ステータス
        form_STR = request.form.get('STR')
        form_STR_option = request.form.get('STR_option')
        form_CON = request.form.get('CON')
        form_CON_option = request.form.get('CON_option')
        form_POW = request.form.get('POW')
        form_POW_option = request.form.get('POW_option')
        form_DEX = request.form.get('DEX')
        form_DEX_option = request.form.get('DEX_option')
        form_APP = request.form.get('APP')
        form_APP_option = request.form.get('APP_option')
        form_SIZ = request.form.get('SIZ')
        form_SIZ_option = request.form.get('SIZ_option')
        form_INT = request.form.get('INT')
        form_INT_option = request.form.get('INT_option')
        form_EDU = request.form.get('EDU')
        form_EDU_option = request.form.get('EDU_option')
        form_hp = request.form.get('hp')
        form_hp_option = request.form.get('hp_option')
        form_mp = request.form.get('mp')
        form_mp_option = request.form.get('mp_option')
        form_ide = request.form.get('ide')
        form_ide_option = request.form.get('ide_option')
        form_luck = request.form.get('luck')
        form_luck_option = request.form.get('luck_option')
        form_knowledge = request.form.get('knowledge')
        form_knowledge_option = request.form.get('knowledge_option')

        # 検索（技能以外）
        # 条件設定
        conditions = []
        if form_name:
            conditions.append(or_(Investigator.name.like(f"%{form_name}%"), Investigator.furigana.like(f"%{form_name}%")))
        if form_Player:
            conditions.append(Investigator.Player.like(f"%{form_Player}%"))
        if form_sex:
            conditions.append(Investigator.sex.like(f"%{form_sex}%"))
        if form_age:
            if(form_age_option == "0"):
                conditions.append(Investigator.age == int(form_age))
            elif(form_age_option == "1"):
                conditions.append(Investigator.age >= int(form_age))
            elif(form_age_option == "2"):
                conditions.append(Investigator.age <= int(form_age))
        if form_STR:
            if(form_STR_option == "0"):
                conditions.append(Investigator.STR_sum == int(form_STR))
            elif(form_STR_option == "1"):
                conditions.append(Investigator.STR_sum >= int(form_STR))
            elif(form_STR_option == "2"):
                conditions.append(Investigator.STR_sum <= int(form_STR))
        if form_CON:
            if(form_CON_option == "0"):
                conditions.append(Investigator.CON_sum == int(form_CON))
            elif(form_CON_option == "1"):
                conditions.append(Investigator.CON_sum >= int(form_CON))
            elif(form_CON_option == "2"):
                conditions.append(Investigator.CON_sum <= int(form_CON))
        if form_POW:
            if(form_POW_option == "0"):
                conditions.append(Investigator.POW_sum == int(form_POW))
            elif(form_POW_option == "1"):
                conditions.append(Investigator.POW_sum >= int(form_POW))
            elif(form_POW_option == "2"):
                conditions.append(Investigator.POW_sum <= int(form_POW))
        if form_DEX:
            if(form_DEX_option == "0"):
                conditions.append(Investigator.DEX_sum == int(form_DEX))
            elif(form_DEX_option == "1"):
                conditions.append(Investigator.DEX_sum >= int(form_DEX))
            elif(form_DEX_option == "2"):
                conditions.append(Investigator.DEX_sum <= int(form_DEX))
        if form_APP:
            if(form_APP_option == "0"):
                conditions.append(Investigator.APP_sum == int(form_APP))
            elif(form_APP_option == "1"):
                conditions.append(Investigator.APP_sum >= int(form_APP))
            elif(form_APP_option == "2"):
                conditions.append(Investigator.APP_sum <= int(form_APP))
        if form_SIZ:
            if(form_SIZ_option == "0"):
                conditions.append(Investigator.SIZ_sum == int(form_SIZ))
            elif(form_SIZ_option == "1"):
                conditions.append(Investigator.SIZ_sum >= int(form_SIZ))
            elif(form_SIZ_option == "2"):
                conditions.append(Investigator.SIZ_sum <= int(form_SIZ))
        if form_INT:
            if(form_INT_option == "0"):
                conditions.append(Investigator.INT_sum == int(form_INT))
            elif(form_INT_option == "1"):
                conditions.append(Investigator.INT_sum >= int(form_INT))
            elif(form_INT_option == "2"):
                conditions.append(Investigator.INT_sum <= int(form_INT))
        if form_EDU:
            if(form_EDU_option == "0"):
                conditions.append(Investigator.EDU_sum == int(form_EDU))
            elif(form_EDU_option == "1"):
                conditions.append(Investigator.EDU_sum >= int(form_EDU))
            elif(form_EDU_option == "2"):
                conditions.append(Investigator.EDU_sum <= int(form_EDU))
        if form_hp:
            if(form_hp_option == "0"):
                conditions.append(Investigator.hp_sum == int(form_hp))
            elif(form_hp_option == "1"):
                conditions.append(Investigator.hp_sum >= int(form_hp))
            elif(form_hp_option == "2"):
                conditions.append(Investigator.hp_sum <= int(form_hp))
        if form_mp:
            if(form_mp_option == "0"):
                conditions.append(Investigator.mp_sum == int(form_mp))
            elif(form_mp_option == "1"):
                conditions.append(Investigator.mp_sum >= int(form_mp))
            elif(form_mp_option == "2"):
                conditions.append(Investigator.mp_sum <= int(form_mp))
        if form_ide:
            if(form_ide_option == "0"):
                conditions.append(Investigator.ide_sum == int(form_ide))
            elif(form_ide_option == "1"):
                conditions.append(Investigator.ide_sum >= int(form_ide))
            elif(form_ide_option == "2"):
                conditions.append(Investigator.ide_sum <= int(form_ide))
        if form_luck:
            if(form_luck_option == "0"):
                conditions.append(Investigator.luck_sum == int(form_luck))
            elif(form_luck_option == "1"):
                conditions.append(Investigator.luck_sum >= int(form_luck))
            elif(form_luck_option == "2"):
                conditions.append(Investigator.luck_sum <= int(form_luck))
        if form_knowledge:
            if(form_knowledge_option == "0"):
                conditions.append(Investigator.knowledge_sum == int(form_knowledge))
            elif(form_knowledge_option == "1"):
                conditions.append(Investigator.knowledge_sum >= int(form_knowledge))
            elif(form_knowledge_option == "2"):
                conditions.append(Investigator.knowledge_sum <= int(form_knowledge))
        
        # 検索
        query = db.session.query(Investigator)
        if conditions:
            query = query.filter(and_(*conditions))
        investigators = query.all()

        # 検索（技能）
        form_skill_conditions = request.form.get('skill_conditions')
        form_skill_conditions_dict = ast.literal_eval(form_skill_conditions)
        for i in range(0, len(form_skill_conditions_dict)):
            condition = form_skill_conditions_dict[i]
            condition_name = condition.get("name")
            condition_value = condition.get("value")
            condition_option = condition.get("option")
            if condition_name and condition_value:
                for j in range(len(investigators)-1, -1, -1):
                    skills = ast.literal_eval(investigators[j].skills)
                    skills_all = []
                    skills_all.extend(skills["battle_skills"])
                    skills_all.extend(skills["search_skills"])
                    skills_all.extend(skills["action_skills"])
                    skills_all.extend(skills["interpersonal_skills"])
                    skills_all.extend(skills["knowledge_skills"])
                    flag = 0
                    for k in range(0, len(skills_all)):
                        skill = skills_all[k]
                        skill_name = skill["name"]
                        if(skill_name == condition_name):
                            initial_points = skill["points"]["initial_points"]
                            job_points = skill["points"]["job_points"]
                            interest_points = skill["points"]["interest_points"]
                            growth_points = skill["points"]["growth_points"]
                            others_points = skill["points"]["others_points"]
                            sum_points = initial_points + job_points + interest_points + growth_points + others_points
                            if(condition_option == "0"):
                                if(int(condition_value) == sum_points):
                                    flag = 1
                            elif(condition_option == "1"):
                                if(int(condition_value) <= sum_points):
                                    flag = 1
                            elif(condition_option == "2"):
                                if(int(condition_value) >= sum_points):
                                    flag = 1
                            break
                    if(flag == 0):
                        investigators.pop(j)

        return render_template('investigator/investigator_list.html', investigators=investigators)
