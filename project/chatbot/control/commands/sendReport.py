from .command import Command
from ..msgTemplate import MsgTemplate
from .report import Report

class SendReport:
 
    def run(self, userId):
        response = [{
            'userId' : 'ReportRoom',
            'msg' : Report.makeReportMsg()
        }]
        #완료 메세지 추가
        return response
    
    def getDescription(self):
        return "Report 메세지 ReportRoom으로 전송합니다."