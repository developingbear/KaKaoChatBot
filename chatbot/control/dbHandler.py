from ..models import User, Answer, Server
from datetime import date, datetime
from chatbot import db

class DBHandler:
    
    @staticmethod
    def isRegistered(userId):
        user = User.query.filter(User.kakao_id == userId).first()
        return True if user else False
        
    @staticmethod
    def isAdmin(userId):
        user = User.query.filter(User.kakao_id == userId).first()
        return True if(user and user.usertype == 'admin') else False

    @staticmethod
    def getUserName(userId):
        user = User.query.filter(User.kakao_id == userId).first()
        return user.name if user else None
    
    @staticmethod
    def getUserStatus(userId):
        user = Answer.query.filter(Answer.checkdate == date.today(),
                                   Answer.kakao_id == userId).first()
        return user.checkstatus if user else None
    
    @staticmethod
    def getUserWorkplace(userId):
        user = Answer.query.filter(Answer.checkdate == date.today(),
                                   Answer.kakao_id == userId).first()
        return user.workplace if user else None
    
    @staticmethod
    def getUserTemperature(userId):
        user = Answer.query.filter(Answer.checkdate == date.today(),
                                   Answer.kakao_id == userId).first()
        return user.temperature if user else None
    
    @staticmethod
    def initToday():
        existList = [user.kakao_id for user in Answer.query.with_entities(Answer.kakao_id).distinct()\
                     .join(User, Answer.kakao_id == User.kakao_id)\
                     .filter(Answer.checkdate == date.today())]        
        userList = User.query.with_entities(User.kakao_id).all()

        for user in userList:
            if user.kakao_id not in existList:
                answer = Answer(kakao_id = user.kakao_id,
                                checkdate = date.today(),
                                checktime = datetime.now(),
                                checkstatus = 'NC')
                db.session.add(answer)
                                      
        db.session.commit()
        
        serverInit = Server.query.filter(Server.date == date.today()).count()
        if not serverInit:
            server = Server(
                        date = date.today(),
                        status = 'ON',
                        firstSend = False,
                        secondSend = False,
                        thirdSend = False,
                        )
            db.session.add(server)
        db.session.commit() 
    
    @staticmethod
    def isServerOn():
        server = Server.query.filter(Server.date == date.today()).first()
        return True if server and server.status == 'ON' else False
    
    @staticmethod
    def setUserWorkPlace(userId, workplace):
        user = Answer.query.filter(Answer.kakao_id == userId,
                                         Answer.checkdate == date.today()).first()
        user.workplace = workplace
        db.session.commit()
        
    @staticmethod
    def setUserTemperature(userId, temperature):
        user = Answer.query.filter(Answer.kakao_id == userId,
                                   Answer.checkdate == date.today()).first()
        user.temperature = temperature
        db.session.commit()
        
    @staticmethod
    def setUserChecktime(userId):
        user = Answer.query.filter(Answer.kakao_id == userId,
                                   Answer.checkdate == date.today()).first()
        user.checktime = datetime.now()
        db.session.commit()
        
    @staticmethod
    def setUserStatusON(userId):
        user = Answer.query.filter(Answer.kakao_id == userId,
                                   Answer.checkdate == date.today()).first()
        user.checkstatus = 'ON'
        db.session.commit()
        
    @staticmethod
    def setUserStatusEND(userId):
        user = Answer.query.filter(Answer.kakao_id == userId,
                                   Answer.checkdate == date.today()).first()
        user.checkstatus = 'END'
        db.session.commit()
        
    @staticmethod
    def initUserAnswer(userId):
        user = Answer.query.filter(Answer.kakao_id == userId,
                                   Answer.checkdate == date.today()).first()
        user.workplace = '출근' #특이사항 없는 경우, 출근이 default
        user.temperature = None
        user.checkstatus = 'NC'
        db.session.commit()
        
    @staticmethod
    def getNCuserList():
        users = Answer.query.filter(Answer.checkdate == date.today(),
                                    Answer.checkstatus == 'NC')
        return users
    
    @staticmethod
    def getONuserList():
        users = Answer.query.filter(Answer.checkdate == date.today(),
                                    Answer.checkstatus == 'ON')
        return users
    
    @staticmethod
    def updateUserStatusByDB(DB_data):
        check_start_time = datetime.strptime("8:30","%H:%M").time()
        check_end_time = datetime.strptime("10:00","%H:%M").time()
                                      
        for email in DB_data:
            curUser = Answer.query.join(User, User.kakao_id == Answer.kakao_id)\
                                  .filter(User.email == email, Answer.checkdate == date.today())\
                                  .first()
            
            #DB에 있는 데이터가 uuser table에는 없을 수도 있음
            if not curUser or curUser.checkstatus != 'NC':
                continue
            
            curUser.workplace = DB_data[email]['workStatus']
            curUser.work_start_time = DB_data[email]['work_start_time']
            curUser.work_end_time = DB_data[email]['work_end_time']
            db.session.commit()
 
            #BP의 경우, 시간 정보가 없는 경우가 존재. 시간 정보가 없는 경우 pass
            if not curUser.work_start_time or not curUser.work_end_time:
                continue
            
            user_work_start_time = datetime.strptime(curUser.work_start_time,"%H:%M").time()
            user_work_end_time = datetime.strptime(curUser.work_end_time, "%H:%M").time()

            if user_work_end_time < check_start_time or user_work_start_time > check_end_time:
                curUser.workplace = '탄력'
            curUser.checkstatus = 'END' if curUser.workplace != '출근' else 'NC'
            
            db.session.commit()

    @staticmethod
    def getTotalCount(group):
        return User.query.filter(User.group == group).count()

    @staticmethod
    def getTodayCheckCount(group, workplace = '출근'):
        checkCount = User.query.join(Answer, Answer.kakao_id == User.kakao_id)\
                               .filter(Answer.checkdate == date.today(),
                                       Answer.workplace == workplace,
                                       User.group == group)\
                               .count()
        return checkCount
    
    @staticmethod
    def getTodayNonCheckCount(group, workplace = '출근'):
        nonCheckCount = User.query.join(Answer, Answer.kakao_id == User.kakao_id)\
                               .filter(Answer.checkdate == date.today(),
                                       Answer.workplace != workplace or Answer.workplace is None,
                                       User.group == group)\
                               .count()
        return nonCheckCount
   
    @staticmethod
    def getTodayWorkplaceList(group, workplace):
        users = User.query.join(Answer, Answer.kakao_id == User.kakao_id)\
                          .filter(Answer.checkdate == date.today(),
                                 Answer.workplace == workplace,
                                 User.group == group)
        targetList = [user.name + '님' for user in users]
        return " ".join(targetList)
    
        
    @staticmethod
    def getTodayUserList():
        users = Answer.query.join(User, Answer.kakao_id == User.kakao_id)\
                           .filter(Answer.checkdate == date.today())
        title = f"📋 UserList {date.today()}\n"
        userList = [f"{user.kakao_id} {user.checkstatus} {user.workplace}" for user in users]
        return title + "\n".join(userList)


    @staticmethod
    def joinTest():
        answer = User.query.join(Answer, User.kakao_id == Answer.kakao_id).count()
        print(answer)
        return answer
    
    @staticmethod
    def deleteUserBy(userId):
        user = User.query.filter(User.kakao_id == userId).first()
        if user :
            db.session.delete(user)
            db.session.commit()
            return f"{userId} was deleted"
        else :
            return "Fail to delete user"
        
        
        