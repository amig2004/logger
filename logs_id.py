from flask import Blueprint, g, request, url_for, Response
from src.database import prepare_db
import json
from . import utils

bp = Blueprint('logs_id', __name__)

@bp.route("/logs/<id>", methods=['GET', 'POST'])
def logs_id(id):
    if request.method == 'GET':
        fields = ['id', 'created', 'person', 'emotion', 'content']
        fields_comments = ['id','log','person','parent_id','created','content']
        db = prepare_db()
        db.execute(f"""
        select lg.id, DATE_FORMAT(lg.created, '%Y-%m-%d %T') created , e.name emotion, p.name person, lg.content from logs lg
            left join emots e
                on e.id = lg.emotion_id
            left join persons p
                on p.id = lg.person_id
            where lg.id={str(id)};""")

        log = db.fetchone()
        print(log)
        db.execute(f"""
        SELECT * FROM comments where log_id={id} group by parent_id order by id desc
        """)
        comments = db.fetchall()
        print(type(log))
        print(comments)
        resp_body = dict(zip(fields, log))
        resp_body['comments'] = [dict(zip(fields_comments, row)) for row in comments]

        return Response(
            json.dumps(resp_body, indent=4), 
            status=200
            )

        #return Response('logs WILL BE HERE - GET\n', status=200)
    elif request.method == 'POST':
        db = prepare_db()
        fields = ['person_id','parent_id','content']
        data = request.json
        print(data)
        if utils.checkData(data, fields):
            # try block to avoid crashing if mysql insert fails
            try:
                print('try block')
                query = f"""
                insert into comments
                (log_id,person_id,parent_id,created,content) 
                values (
                    {str(id)},
                    {str(data['person_id'])},
                    {str(data['parent_id'])},
                    NOW(),
                    '{str(data['content_id'])}');
                """
                print(query)
                #g.db.execute(query)

                #g.dbhandler.commit()
                return Response(status=201)
            except Exception as e:
                return Response(e, status=500)

            
        else:
            return Response(status=400)
        return Response(status=200)
    else:  
        return Response(status=405)


