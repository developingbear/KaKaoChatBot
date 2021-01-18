from .command import Command
from chatbot.control.dbHandler import DBHandler

class Init(Command):

    def run(self, userId):
        '''
        from apscheduler.schedulers.background import BackgroundScheduler
        scheduler = BackgroundScheduler(daemon=True)
        scheduler.add_job(Init.initDB, 'cron', hour = 0, minute = 48, second='10') # 'cron', hour='0', minute='0', second='1')
        scheduler.start()
        '''
        DBHandler.initToday()
        response = [{
            'userId' : userId,
            'msg' : '✅ First Init done'
        }]
        return response
 
    def getDescription(self):
        return "오늘 DB answer row를 init 합니다."#"Daily DB init Schedule를 등록합니다. 이 작업은 Server를 실행한 뒤, 한 번만 필요합니다."