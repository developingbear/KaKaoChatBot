from .command import Command

class Help(Command):
    
    adminCmds = ''
    def __init__(self, cmdlist):
        Help.adminCmds = cmdlist
    
    def run(self, userId):
        response = [{
            'userId' : userId,
            'msg' : Help.gethelpMsg()
        }]
        
        return response
    
    def getDescription(self):
        return "도움말을 조회합니다."
    
    @staticmethod
    def gethelpMsg():
        helpMsg = [f'💬 [{cmd}] : {Help.adminCmds[cmd].getDescription()}'for cmd in Help.adminCmds]
        return "\n\n".join(helpMsg)