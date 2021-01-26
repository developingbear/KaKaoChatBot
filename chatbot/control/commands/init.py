from .command import Command
from chatbot.control.dbHandler import DBHandler
from chatbot import create_app

class Init(Command):

    def run(self, userId):
        response = [{
            'userId' : userId,
            'msg' : '✅ manual Init done'
        }]
        DBHandler.initToday()
        return response
    
    @staticmethod
    def DBtoday(app):
        with app.app_context():
            DBHandler.initToday()
            print("init done")
 
    def getDescription(self):
        return "오늘 DB answer row를 init 합니다."