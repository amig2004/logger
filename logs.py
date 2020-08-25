from flask import Blueprint, g, request, url_for, Response
from src.database import prepare_db
import json
from . import utils

bp = Blueprint('logs', __name__)

@bp.route("/logs", methods=['GET', 'POST'])
def logs():
    if request.method == 'GET':
        

        return Response('logs WILL BE HERE - GET\n', status=200)
    elif request.method == 'POST':
        return Response('logs WILL BE HERE - POST\n', status=200)