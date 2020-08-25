from flask import Flask
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

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    #database initialization
    from . import database
    database.init_app(app)

    #register views here
    from . import (tags, persons, logs)
    app.register_blueprint(tags.bp)
    app.register_blueprint(persons.bp)
    app.register_blueprint(logs.bp)

    #DEBUG
    # print('URL_RULES:', app.url_map)
    # print('CONFIG', app.config)

    return app

