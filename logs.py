from flask import Blueprint, g, request, url_for, Response
from src.database import prepare_db
import json
from . import utils

bp = Blueprint('logs', __name__)

@bp.route("/logs", methods=['GET', 'POST'])
def logs():
    if request.method == 'GET':
        fields = ['id', 'created', 'person', 'emotion', 'content']
        db = prepare_db()
        db.execute("""
        select lg.id, lg.created, e.name, p.name, lg.content from logs lg
            join emots e
                on e.id = lg.emotion_id
            join persons p
                on p.id = lg.person_id;"""
                )
        logs = db.fetchall()

        resp_body = [dict(zip(fields, row)) for row in logs]

        return Response(
            json.dumps(resp_body, indent=4), 
            status=200
            )

        #return Response('logs WILL BE HERE - GET\n', status=200)
    elif request.method == 'POST':
        fields = ['emotion_id','content','person_id' ]
        data = request.json

        if utils.checkData(data, fields):


        return Response('logs WILL BE HERE - POST\n', status=200)


