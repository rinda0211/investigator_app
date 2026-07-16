import os
from investigator_app import app
from investigator_app import db

app.app_context().push()

db_path = 'instance/investigator_list.db'
if os.path.exists(db_path):
    os.remove(db_path)

db.create_all()
exit()