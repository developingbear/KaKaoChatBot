from .command import Command
from chatbot.control.dbHandler import DBHandler
from ..msgTemplate import MsgTemplate
from datetime import date

class Report(Command):

    def run(self, userId):
        response = [{
            'userId' : userId,
            'msg' :  Report.makeReportMsg()
        }]
        return response
    
    def getDescription(self):
        return "Report 메세지를 생성합니다."
    
    @staticmethod
    def makeReportMsg():
        homeworkingList = DBHandler.getTodayWorkplaceList('DS사업1)e커머스팀', '재택')
        vacationList = DBHandler.getTodayWorkplaceList('DS사업1)e커머스팀', '휴가')
        workoutsideList = DBHandler.getTodayWorkplaceList('DS사업1)e커머스팀', '외근')
        flexibleworkList = DBHandler.getTodayWorkplaceList('DS사업1)e커머스팀', '탄력')
        newline = '\n'
        return f'''
📋 오쇼핑IT서비스팀
{date.today()}

✅ 총 인원 : {DBHandler.getTotalCount('DS사업1)e커머스팀')}
✅ 진행 인원 : {DBHandler.getTodayCheckCount('DS사업1)e커머스팀')}
✅ 부재 인원 : {DBHandler.getTodayNonCheckCount('DS사업1)e커머스팀')}
{newline + '▪ 재택 : ' + homeworkingList if homeworkingList else ""}{newline + '▪ 휴가 : ' + vacationList if vacationList else ""}{newline + '▪ 외근 : ' + workoutsideList if workoutsideList else ""}{newline + '▪ 탄력 : ' + flexibleworkList if flexibleworkList else ""}

✅ 진행인원 중 이상체온 인원 : 0

✅ 협력사 총원 32명 중 {DBHandler.getTodayCheckCount('BP_DS사업1)e커머스팀')}명 출근 : 전원 정상

챗봇 관련 문의는 문창주님에게 부탁드립니다.
'''