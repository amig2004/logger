from flask import Flask, Blueprint, url_for
from flask import Response
import json
import pymysql
import utils

# prepare views

# prepare databse connection
dbcfg_file = open('config.json', 'r')
dbcfg = json.load(dbcfg_file)

print('HOST: ', dbcfg['host'])
try:
    dbahndler = pymysql.connect(
        host=dbcfg['host'],
        user=dbcfg['user'],
        password=dbcfg['pass'],
        database=dbcfg['dbname']
        )
    db = dbahndler.cursor()
    print("INFO: database loaded")

except Exception as e:
    print('DB Error: ', e)
    exit(-1)

app = Flask(__name__)

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


@app.route("/tags", methods=['GET'])
def tags():
    fields = ['id', 'name']
    if request.method == 'GET':
        tagslist = []

        #obtain data from db
        cursor.execute('SELECT * FROM tags')
        tags = cursor.fetchall()
        for row in tags:
            tagslist.append(dict.fromkeys(fields, row))
        
        return Response(
            json.dump(tagslist, indent=4), 
            status=200
            )

    elif request.method == 'POST':
        data = json.dumps(
            request.json()
            )

        # if data is correct -> insert to database
        # TODO special marks detection, to avoid sql injection etc.
        if utils.checkData(data, fields)
            cursor.execute(f'INSERT INTO tags (name) VALUES {data.name}'')
            
            return Response(status=201)
        else:
            return Response(status=400)

    else:  
        return Response(status=405)
            
@app.route("/persons", methods=['GET', 'POST'])
def persons():
    if request.method == 'GET':
        return Response('PERSONS WILL BE HERE - GET\n', status=200)
    elif request.method == 'POST':
        return Response('PERSONS WILL BE HERE - POST\n', status=200)

@app.route("/logs")
def logs():
    if request.method == 'GET':
        return Response('LOGS WILL BE HERE - GET\n', status=200)
    elif request.method == 'POST':
        return Response('LOGS WILL BE HERE - POST\n', status=200)




if __name__ == '__main__':
    for rule in app.url_map.iter_rules():
        print(rule.endpoint)
    app.run(debug=True)

    dbahndler.close()

