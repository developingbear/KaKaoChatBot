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
    def DBtoday():
        app = create_app()
        with app.app_context():
            DBHandler.initToday()
 
    def getDescription(self):
        return "오늘 DB answer row를 init 합니다."#"Daily DB init Schedule를 등록합니다. 이 작업은 Server를 실행한 뒤, 한 번만 필요합니다."