import pymysql
from flask import current_app, g
import json

def prepare_db():
    try:
        if 'dbhandler' not in g:
            g.dbhandler = pymysql.connect(
                host=current_app.config['DATABASE']['host'],
                user=current_app.config['DATABASE']['user'],
                password=current_app.config['DATABASE']['pass'],
                database=current_app.config['DATABASE']['dbname']
                )
            g.db = g.dbhandler.cursor()
            print("INFO: database loaded")
            return g.db
    
    except Exception as e:
        print('DB ERROR: ', e)
        exit(-1)

def disconnect_db(e=None):
    if hasattr(g, 'db'):
        g.db.close()
        print('DB CLOSED')

def init_app(app):
    app.teardown_appcontext(disconnect_db)