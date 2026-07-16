from flask import render_template, request, redirect, url_for

from sqlalchemy import and_
from sqlalchemy import or_

from investigator_app import app
from investigator_app import db
from investigator_app.models.investigator import Investigator
from investigator_app.models.investigator import Session

import ast, datetime, json, math

@app.route('/add_session', methods=['GET', 'POST'])
def add_session():
    if request.method == 'GET':
        investigators = Investigator.query.all()
        return render_template('session/add_session.html', investigators=investigators)
    if request.method == 'POST':
        form_session_name = request.form.get('senario_name')

        form_date1 = request.form.get('date1')
        if form_date1: form_date1_date = datetime.date.strptime(form_date1, '%Y-%m-%d')
        else: form_date1_date = None
        form_date2 = request.form.get('date2')
        if form_date2: form_date2_date = datetime.date.strptime(form_date2, '%Y-%m-%d')
        else: form_date2_date = None
        form_date3 = request.form.get('date3')
        if form_date3: form_date3_date = datetime.date.strptime(form_date3, '%Y-%m-%d')
        else: form_date3_date = None
        form_date4 = request.form.get('date4')
        if form_date4: form_date4_date = datetime.date.strptime(form_date4, '%Y-%m-%d')
        else: form_date4_date = None
        form_date5 = request.form.get('date5')
        if form_date5: form_date5_date = datetime.date.strptime(form_date5, '%Y-%m-%d')
        else: form_date5_date = None
        form_date6 = request.form.get('date6')
        if form_date6: form_date6_date = datetime.date.strptime(form_date6, '%Y-%m-%d')
        else: form_date6_date = None
        form_date7 = request.form.get('date7')
        if form_date7: form_date7_date = datetime.date.strptime(form_date7, '%Y-%m-%d')
        else: form_date7_date = None
        form_date8 = request.form.get('date8')
        if form_date8: form_date8_date = datetime.date.strptime(form_date8, '%Y-%m-%d')
        else: form_date8_date = None
        form_date9 = request.form.get('date9')
        if form_date9: form_date9_date = datetime.date.strptime(form_date9, '%Y-%m-%d')
        else: form_date9_date = None
        form_date10 = request.form.get('date10')
        if form_date10: form_date10_date = datetime.date.strptime(form_date10, '%Y-%m-%d')
        else: form_date10_date = None

        form_kp = request.form.get('KP', default=None)
        form_kpc = request.form.get('KPC_name', default=None)
        form_kpc_id = request.form.get('KPC', default=None, type=int)

        form_skp1 = request.form.get('SKP1', default=None)
        form_skpc1 = request.form.get('SKPC1_name', default=None)
        form_skpc1_id = request.form.get('SKPC1', default=None, type=int)
        form_skp2 = request.form.get('SKP2', default=None)
        form_skpc2 = request.form.get('SKPC2_name', default=None)
        form_skpc2_id = request.form.get('SKPC2', default=None, type=int)
        form_skp3 = request.form.get('SKP3', default=None)
        form_skpc3 = request.form.get('SKPC3_name', default=None)
        form_skpc3_id = request.form.get('SKPC3', default=None, type=int)

        form_pl1 = request.form.get('PL1', default=None)
        form_pc1 = request.form.get('PC1_name', default=None)
        form_pc1_id = request.form.get('PC1', default=None, type=int)
        form_pl2 = request.form.get('PL2', default=None)
        form_pc2 = request.form.get('PC2_name', default=None)
        form_pc2_id = request.form.get('PC2', default=None, type=int)
        form_pl3 = request.form.get('PL3', default=None)
        form_pc3 = request.form.get('PC3_name', default=None)
        form_pc3_id = request.form.get('PC3', default=None, type=int)
        form_pl4 = request.form.get('PL4', default=None)
        form_pc4 = request.form.get('PC4_name', default=None)
        form_pc4_id = request.form.get('PC4', default=None, type=int)
        form_pl5 = request.form.get('PL5', default=None)
        form_pc5 = request.form.get('PC5_name', default=None)
        form_pc5_id = request.form.get('PC5', default=None, type=int)
        form_pl6 = request.form.get('PL6', default=None)
        form_pc6 = request.form.get('PC6_name', default=None)
        form_pc6_id = request.form.get('PC6', default=None, type=int)
        form_pl7 = request.form.get('PL7', default=None)
        form_pc7 = request.form.get('PC7_name', default=None)
        form_pc7_id = request.form.get('PC7', default=None, type=int)
        form_pl8 = request.form.get('PL8', default=None)
        form_pc8 = request.form.get('PC8_name', default=None)
        form_pc8_id = request.form.get('PC8', default=None, type=int)
        form_pl9 = request.form.get('PL9', default=None)
        form_pc9 = request.form.get('PC9_name', default=None)
        form_pc9_id = request.form.get('PC9', default=None, type=int)
        form_pl10 = request.form.get('PL10', default=None)
        form_pc10 = request.form.get('PC10_name', default=None)
        form_pc10_id = request.form.get('PC10', default=None, type=int)
        session = Session(
            senario_name = form_session_name,
            date1 = form_date1_date,
            date2 = form_date2_date,
            date3 = form_date3_date,
            date4 = form_date4_date,
            date5 = form_date5_date,
            date6 = form_date6_date,
            date7 = form_date7_date,
            date8 = form_date8_date,
            date9 = form_date9_date,
            date10 = form_date10_date,
            KP = form_kp,
            KPC = form_kpc,
            KPC_id = form_kpc_id,
            SKP1 = form_skp1,
            SKPC1 = form_skpc1,
            SKPC1_id = form_skpc1_id,
            SKP2 = form_skp2,
            SKPC2 = form_skpc2,
            SKPC2_id = form_skpc2_id,
            SKP3 = form_skp3,
            SKPC3 = form_skpc3,
            SKPC3_id = form_skpc3_id,
            PL1 = form_pl1,
            PC1 = form_pc1,
            PC1_id = form_pc1_id,
            PL2 = form_pl2,
            PC2 = form_pc2,
            PC2_id = form_pc2_id,
            PL3 = form_pl3,
            PC3 = form_pc3,
            PC3_id = form_pc3_id,
            PL4 = form_pl4,
            PC4 = form_pc4,
            PC4_id = form_pc4_id,
            PL5 = form_pl5,
            PC5 = form_pc5,
            PC5_id = form_pc5_id,
            PL6 = form_pl6,
            PC6 = form_pc6,
            PC6_id = form_pc6_id,
            PL7 = form_pl7,
            PC7 = form_pc7,
            PC7_id = form_pc7_id,
            PL8 = form_pl8,
            PC8 = form_pc8,
            PC8_id = form_pc8_id,
            PL9 = form_pl9,
            PC9 = form_pc9,
            PC9_id = form_pc9_id,
            PL10 = form_pl10,
            PC10 = form_pc10,
            PC10_id = form_pc10_id
        )
        db.session.add(session)
        db.session.commit()

        return redirect(url_for('index'))