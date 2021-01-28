from .command import Command
from ..msgTemplate import MsgTemplate
from .report import Report

class SendReport:
 
    def run(self, userId):
        response = [{
            'userId' : 'ReportRoom ons박철희',
            'msg' : Report.makeReportMsg()
        }]
        #완료 메세지 추가
        return response
    
    def getDescription(self):
        return "Report 메세지를 ReportRoom과 팀장님에게 전송합니다."