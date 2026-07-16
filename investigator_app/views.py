from flask import render_template, request, redirect, url_for

from sqlalchemy import and_
from sqlalchemy import or_

from investigator_app import app
from investigator_app import db
from investigator_app.models.investigator import Investigator

import ast, json, math

# 変数
from investigator_app.data.skills_default import skills_default

# メニュー画面
# MARK: investigator_app.templates.index
import investigator_app.routes.index

# 探索者追加画面
import investigator_app.routes.investigator.add_investigator
# 探索者一覧画面
import investigator_app.routes.investigator.investigator_list
# 探索者検索画面
import investigator_app.routes.investigator.search_investigator
# 探索者閲覧画面
import investigator_app.routes.investigator.view_investigator
# 探索者編集画面
import investigator_app.routes.investigator.edit_investigator
# 探索者削除API
import investigator_app.routes.investigator.delete_investigator
# 探索者ココフォリアコマ出力API
import investigator_app.routes.investigator.copy_investigator
# 探索者保存API
import investigator_app.routes.investigator.save_investigator
# 探索者全保存API
import investigator_app.routes.investigator.save_investigator_all
# 探索者読み込み画面
import investigator_app.routes.investigator.load_investigator

# セッション追加画面
import investigator_app.routes.session.add_session
# セッション一覧
import investigator_app.routes.session.session_list
# セッション編集画面
import investigator_app.routes.session.edit_session
# セッション削除API
import investigator_app.routes.session.delete_session
# セッション保存API
import investigator_app.routes.session.save_session
# セッション保存API
import investigator_app.routes.session.save_session_all
# セッション読み込み画面
import investigator_app.routes.session.load_session

# デバッグ用浅中キャラシ追加
import investigator_app.routes.debug.add_asanakauta