import pymysql
from flask import current_app, g

def prepare_db(dbcfg: dict):
    print('HOST: ', dbcfg['host'])
    try:
        if 'dbhandler' not in g:
            g.dbhandler = pymysql.connect(
                host=dbcfg['host'],
                user=dbcfg['user'],
                password=dbcfg['pass'],
                database=dbcfg['dbname']
                )
            g.db = dbahndler.cursor()
            print("INFO: database loaded")
            return g.db
    
    except Exception as e:
        print('DB ERROR: ', e)
        exit(-1)

@app.teardown_appcontext
def disconnect_db():
    if hasattr(g, 'db'):
        g.db.close()
