from flask import Flask, Blueprint, url_for, request
from flask import Response, teardown_appcontext
from flask import current_app, g
import json
import pymysql
import utils

app = Flask(__name__)

dbcfg_file = open('config.json', 'r')
dbcfg = json.load(dbcfg_file)


@app.route("/", methods=['GET'])
def site_map():
    links = {
        "tags": "qertqrtqert",
        "persons": "qeryyqeryeryqeryq",
        "logs": "qeryqeyqeryqery"
    }

    return Response( 
        json.dumps(links, indent=4),
        status=200
        )


@app.route("/tags", methods=['GET', 'POST'])
def tags():
    db = prepare_db()
    fields = ['id', 'name']
    if request.method == 'GET':
        tagslist = []

        #obtain data from db
        db.execute('SELECT * FROM tags')
        tags = db.fetchall()
        for row in tags:
            tagslist.append(
                dict(zip(fields, row))
                )
        
        resp_value = str()
        return Response(
            json.dumps(tagslist, indent=4), 
            status=200
            )

    elif request.method == 'POST':
        # delete id ( marked as AI in db, not req)
        fields = ['name']
        print('RECEIVED: ', request.data)
        print('TAG TYPE:', type(request.data))
        data = request.json
        print('TAG TYPE:', type(data))
        print('NEW TAG:', data)
        # if data is correct -> insert to database
        # TODO special marks detection, to avoid sql injection etc.
        # if utils.checkData(data, fields):
        #     # try block to avoid crashing if mysql insert fails
        #     try:
        #         db.execute(f'INSERT INTO tags (name) VALUES {data.name}')
        #     except Exception as e:
        #         return Response(e, status=500)

        #     return Response(status=201)
        # else:
        #     return Response(status=400)
        return Response(status=200)
    else:  
        return Response(status=405)
            
@app.route("/persons", methods=['GET', 'POST'])
def persons():
    if request.method == 'GET':
        return Response('PERSONS WILL BE HERE - GET\n', status=200)
    elif request.method == 'POST':
        return Response('PERSONS WILL BE HERE - POST\n', status=200)

@app.route("/logs", methods=['GET', 'POST'])
def logs():
    if request.method == 'GET':
        return Response('LOGS WILL BE HERE - GET\n', status=200)
    elif request.method == 'POST':
        return Response('LOGS WILL BE HERE - POST\n', status=200)


@app.route("/addcomment", methods=['POST'])
def addcomment():
    # extract  dictionary from json, check corectness

    # if everything is ok -> insert to db
    return Response('COMMENT ADDITION WILL BE HERE', status=200)

if __name__ == '__main__':
    app.run(debug=True)

    dbahndler.close()
