from .command import Command
from chatbot.control.dbHandler import DBHandler

class Delete(Command):
    
    def run(self, userId):
        response = [{
            'userId' : userId,
            'msg' : DBHandler.deleteUserBy(userId)
        }]
        return response
    
    def getDescription(self):
        return "UserId로 User를 삭제합니다"