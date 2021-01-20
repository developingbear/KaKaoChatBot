from .command import Command
from chatbot.control.dbHandler import DBHandler

class Show(Command):
    
    def run(self, userId):
        response = [{
            'userId' : userId,
            'msg' : DBHandler.getTodayUserList()
        }]
        return response
    
    def getDescription(self):
        return "현재 User들의 응답 상태를 확인합니다."