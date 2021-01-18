from .command import Command
from chatbot.control.dbHandler import DBHandler
from ..msgTemplate import MsgTemplate
from datetime import datetime

class Alarm(Command):
    
    def run(self, userId):
        NC = 0
        ON = 1
        alarmResponse = [
            {
                'userId' : '',
                'msg' : MsgTemplate.getFormMsg(),
            }, 
            {
                'userId' : '',
                'msg' : MsgTemplate.getTemperAskMsg(),
            } 
        ]
        users = DBHandler.getNCuserList()
        for user in users:
            if user.work_start_time and Alarm.isWorkTime(user.work_start_time):
                print(user.kakao_id, user.work_start_time)
                alarmResponse[NC]['userId'] += user.kakao_id + " "
            elif not user.work_start_time :
                alarmResponse[NC]['userId'] += user.kakao_id + " "
                
        users = DBHandler.getONuserList()
        for user in users:
            alarmResponse[ON]['userId'] += user.kakao_id + " "
                
        sample =[{
            'userId' : 'ons문창주',
            'msg' : 'test'
        }]
        print(alarmResponse[NC])
        print(alarmResponse[ON])
        #return sample
        return alarmResponse
    
    @staticmethod
    def isWorkTime(work_start_time):
        work_start_time = datetime.strptime(work_start_time, "%H:%M").time()
        cur_time = datetime.now().time()
        return True if cur_time > work_start_time else False
    
    def getDescription(self):
        return "미응답 유저들을 대상으로 근무시작 시간과 현재시간과 비교한뒤 알람메세지를 전송합니다."
        