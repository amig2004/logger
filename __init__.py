from flask import Flask,Response
import os 
import json

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE = json.load(
            open(os.path.join(app.root_path, 'config.json'),'r')
        ),
    )

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a site map
    @app.route('/')
    def site_map():
        links = {
            "tags": "/tags",
            "persons": "/persons",
            "logs": "/logs",
            "specified_log + comments": "/logs/<id:int>"
        }

        return Response( 
            json.dumps(links, indent=4),
            status=200
            )

    #database initialization
    from . import database
    database.init_app(app)

    #register views here
    from . import (tags, persons, logs, logs_id)
    app.register_blueprint(tags.bp)
    app.register_blueprint(persons.bp)
    app.register_blueprint(logs.bp)
    app.register_blueprint(logs_id.bp)
    #DEBUG
    # print('URL_RULES:', app.url_map)
    # print('CONFIG', app.config)

    return app

