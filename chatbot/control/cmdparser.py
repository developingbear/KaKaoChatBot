from .commands.init import Init
from .commands.show import Show
from .commands.alarm import Alarm
from .commands.report import Report
from .commands.sendReport import SendReport
from .commands.help import Help
from .commands.delete import Delete

class CmdParser:
    adminCmds = {
        'init' : Init(),
        'show' : Show(),
        'alarm': Alarm(),
        're': Report(),
        'sr': SendReport(),
        'del' : Delete(),
    }
    adminCmds['help'] = Help(adminCmds)
    
    @staticmethod
    def isAdminCommand(msg):
        return True if msg in CmdParser.adminCmds else False
    
    @staticmethod
    def run(userId, userMsg):
        response = CmdParser.adminCmds[userMsg].run(userId)
        return response
