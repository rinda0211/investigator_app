from flask import render_template, request, redirect, url_for

from sqlalchemy import and_
from sqlalchemy import or_

from investigator_app import app
from investigator_app import db
from investigator_app.models.investigator import Investigator
from investigator_app.models.investigator import Session

import ast, datetime, json, math

@app.route('/edit_session/<int:id>', methods=['GET', 'POST'])
def edit_session(id):
    if request.method == 'GET':
        investigators = Investigator.query.all()
        session = Session.query.get_or_404(id)
        return render_template('session/edit_session.html', investigators=investigators, session = session)
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

        # 更新
        session = Session.query.get(id)
        session.senario_name = form_session_name
        session.date1 = form_date1_date
        session.date2 = form_date2_date
        session.date3 = form_date3_date
        session.date4 = form_date4_date
        session.date5 = form_date5_date
        session.date6 = form_date6_date
        session.date7 = form_date7_date
        session.date8 = form_date8_date
        session.date9 = form_date9_date
        session.date10 = form_date10_date
        session.KP = form_kp
        session.KPC = form_kpc
        session.KPC_id = form_kpc_id
        session.SKP1 = form_skp1
        session.SKPC1 = form_skpc1
        session.SKPC1_id = form_skpc1_id
        session.SKP2 = form_skp2
        session.SKPC2 = form_skpc2
        session.SKPC2_id = form_skpc2_id
        session.SKP3 = form_skp3
        session.SKPC3 = form_skpc3
        session.SKPC3_id = form_skpc3_id
        session.PL1 = form_pl1
        session.PC1 = form_pc1
        session.PC1_id = form_pc1_id
        session.PL2 = form_pl2
        session.PC2 = form_pc2
        session.PC2_id = form_pc2_id
        session.PL3 = form_pl3
        session.PC3 = form_pc3
        session.PC3_id = form_pc3_id
        session.PL4 = form_pl4
        session.PC4 = form_pc4
        session.PC4_id = form_pc4_id
        session.PL5 = form_pl5
        session.PC5 = form_pc5
        session.PC5_id = form_pc5_id
        session.PL6 = form_pl6
        session.PC6 = form_pc6
        session.PC6_id = form_pc6_id
        session.PL7 = form_pl7
        session.PC7 = form_pc7
        session.PC7_id = form_pc7_id
        session.PL8 = form_pl8
        session.PC8 = form_pc8
        session.PC8_id = form_pc8_id
        session.PL9 = form_pl9
        session.PC9 = form_pc9
        session.PC9_id = form_pc9_id
        session.PL10 = form_pl10
        session.PC10 = form_pc10
        session.PC10_id = form_pc10_id

        db.session.merge(session)
        db.session.commit()

        return redirect(url_for('session_list'))