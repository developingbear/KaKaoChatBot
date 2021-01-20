from .dbHandler import DBHandler

class MsgTemplate:
    
    @staticmethod
    def getFormMsg():
        return  '''
📋 오늘의 근무 형태는 무엇인가요?

✅ 1. 출근
✅ 2. 재택
✅ 3. 휴무
✅ 4. 외근
✅ 5. 탄력

❗해당 번호로 입력해주세요
▪ 출근인 경우 ➡ 1
▪ 휴무인 경우 ➡ 3
'''
    
    @staticmethod
    def getEndMsg(userId):
        workplace = DBHandler.getUserWorkplace(userId)
        return f'''
✅ 완료
▪ {DBHandler.getUserName(userId)}님 {workplace} {DBHandler.getUserTemperature(userId) if workplace == '출근' else ""} 기록❗
▪ 수정을 원하시면 [수정] 입력❗
'''

    @staticmethod
    def getRemindMsg():
        return "\n🤔 오늘 설문에 이미 응답하셨어요\n▪ 수정을 원하시면 [수정]을 입력❗\n"
    
    @staticmethod
    def getInvalidMsg():
        return "\n🤔 잘못된 입력입니다\n▪ 다시 입력해주세요❗\n"

    @staticmethod
    def getTemperErrorMsg():
        return "\n🤔 잘못된 체온인것 같아요!\n▪ 다시 입력해주세요❗\n"
    
    @staticmethod
    def getTemperAskMsg():
        return "\n🌡 오늘의 체온은 몇 도 인가요❓\n▪ 숫자만 입력해주세요\n"
    
    @staticmethod
    def getInvaildUserMsg():
        return "\n🙅 등록되지 않은 사용자입니다❗\n▪ 관리자에게 문의바랍니다.\n"
    
    @staticmethod
    def getSurveyEndMsg():
        return "\n❌ 금일 설문이 종료되었습니다❗\n"