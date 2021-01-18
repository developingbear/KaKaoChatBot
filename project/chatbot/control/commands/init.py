from .command import Command
from chatbot.control.dbHandler import DBHandler

class Init(Command):

    def run(self, userId):
        from apscheduler.apscheduler.background import BackgroundScheduler
        scheduler = BackgroundScheduler()
        scheduler.add_job(Init.initDB(), 'cron', hour='0', minute='0', second='1')
        scheduler.start()
        response = [{
            'userId' : userId,
            'msg' : '✅ First Init done'
        }]
        return response

    @staticmethod
    def initDB():
        DBHandler.initToday()

    def getDescription(self):
        return "Daily DB init Schedule를 등록합니다. 이 작업은 Server를 실행하 후, 한 번만 필요합니다."