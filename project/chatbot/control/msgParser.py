from .dbHandler import DBHandler
from .cmdparser import CmdParser
from .msgTemplate import MsgTemplate

class Msgparser:
    @staticmethod
    def run(userData):
        singleType = 0
        userId = userData['id']
        userMsg = userData['msg']
        response = [{'userId' : userId, 'msg' : ""}]
        
        if not DBHandler.isRegistered(userId):
            response[singleType]['msg'] = MsgTemplate.getInvaildUserMsg()
        elif DBHandler.isAdmin(userId) and CmdParser.isAdminCommand(userMsg):
            response = CmdParser.run(userId, userMsg)
        else:
            response[singleType]['msg'] = Msgparser.check(userId, userMsg)
        return response
    
    @staticmethod
    def check(userId, userMsg):
        userStatus = DBHandler.getUserStatus(userId)
        
        if DBHandler.isServerOn():
            ### 
            if userStatus == 'NC':
                options = {"1" : "출근", "2" : "재택", "3" : "휴무", "4" : "외근", "5" : "탄력"}
                if userMsg in options:
                    DBHandler.setUserWorkPlace(userId, options[userMsg])
                    if options[userMsg] == "출근":
                        DBHandler.setUserStatusON(userId)
                        return MsgTemplate.getTemperAskMsg()
                    else :
                        return Msgparser.setUserEND(userId)
                else :
                    return MsgTemplate.getInvalidMsg()
            ###   
            if userStatus == 'ON':
                if Msgparser.isValidTemperature(userMsg):
                    DBHandler.setUserTemperature(userId, userMsg)
                    return Msgparser.setUserEND(userId)
                else:
                    return MsgTemplate.getTemperErrorMsg()
            ###
            if userStatus == 'END':
                if userMsg == '수정':
                    DBHandler.initUserAnswer(userId)
                    return MsgTemplate.getFormMsg()
                else :
                    return MsgTemplate.getRemindMsg()
        else:#serverOFF
            return MsgTemplate.getSurveyEndMsg()
        
    @staticmethod
    def setUserEND(userId):
        DBHandler.setUserStatusEND(userId)
        DBHandler.setUserChecktime(userId)
        return MsgTemplate.getEndMsg(userId)

    @staticmethod
    def isValidTemperature(value):
        try:
            float(value)
        except ValueError:
            return False
        return True if 35 <= float(value) <= 41 else False