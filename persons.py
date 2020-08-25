from flask import Blueprint, g, request, url_for, Response
from src.database import prepare_db
import json
from . import utils

bp = Blueprint('persons', __name__)

@bp.route("/persons", methods=['GET', 'POST'])
def persons():
    
    fields = ['id', 'name']
    if request.method == 'GET':
        db = prepare_db()
        personslist = []

        #obtain data from db
        db.execute('SELECT * FROM persons')
        persons = db.fetchall()
        for row in persons:
            personslist.append(
                dict(zip(fields, row))
                )
        
        return Response(
            json.dumps(personslist, indent=4), 
            status=200
            )

    elif request.method == 'POST':
        db = prepare_db()
        # delete id ( marked as AI in db, not req)
        fields = ['name']
        data = request.json
        print('TAG TYPE:', type(data))
        print('NEW TAG:', data)
        # if data is correct -> insert to database
        # TODO special marks detection, to avoid sql injection etc.
        if utils.checkData(data, fields):
            # try block to avoid crashing if mysql insert fails
            try:
                print('TRY BLCOK')
                g.db.execute(f"insert into persons (name) values ('{data['name']}');")
                g.dbhandler.commit()
                return Response(status=201)
            except Exception as e:
                print('EXCEPTION block')
                return Response(e, status=500)

            
        else:
            return Response(status=400)
        return Response(status=200)
    else:  
        return Response(status=405)