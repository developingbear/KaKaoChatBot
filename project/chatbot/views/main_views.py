from flask import Blueprint, request
from chatbot.control.msgParser import Msgparser
from chatbot.control.dbHandler import DBHandler
import json

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/check/<userData>')
def run(userData):
    result = Msgparser.run(json.loads(userData))
    return json.dumps(result)

@bp.route('/cjdb', methods=['POST'])
def getDBdata():
    dbData = json.loads(request.get_json())
    DBHandler.updateUserStatusByDB(dbData)
    return ""