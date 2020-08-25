from flask import Blueprint, g, request, url_for, Response
from src.database import prepare_db
import json
from . import utils
import datetime

bp = Blueprint('logs', __name__)

@bp.route("/logs", methods=['GET', 'POST'])
def logs():
    if request.method == 'GET':
        fields = ['id', 'created', 'person', 'emotion', 'content']
        db = prepare_db()
        db.execute("""
        select lg.id, DATE_FORMAT(lg.created, '%Y-%m-%d %T') created , e.name emotion, p.name person, lg.content from logs lg
            left join emots e
                on e.id = lg.emotion_id
            left join persons p
                on p.id = lg.person_id;"""
                )
        logs = db.fetchall()
        # for row in logs:
        #     print(logs)
        resp_body = [dict(zip(fields, row)) for row in logs]
        
        print(resp_body)
        print(type(resp_body))
        
        return Response(
            json.dumps(resp_body, indent=4), 
            status=200
            )

        #return Response('logs WILL BE HERE - GET\n', status=200)
    elif request.method == 'POST':
        db = prepare_db()
        fields = ['emotion_id', 'content', 'person_id']
        data = request.json

        print(type(data['emotion_id']))
        print(type(data['content']))
        print(type(data['person_id']))
        if utils.checkData(data, fields):
            # try block to avoid crashing if mysql insert fails
            # try:
                query=f"""
                insert into logs (emotion_id, content, person_id) 
                values (
                    {str(data['emotion_id'])}, 
                    '{data['content']}',
                    {str(data['person_id'])});
                """
                print(query)
                g.db.execute(query)
                
                g.dbhandler.commit()
                return Response(status=201)
            # except Exception as e:
            #     return Response(e, status=500)

            
        else:
            return Response(status=400)
        return Response(status=200)
    else:  
        return Response(status=405)