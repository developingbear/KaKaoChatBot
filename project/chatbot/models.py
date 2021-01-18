#db는 __init__.py에서 생성한 SQLAlchemy객체
from chatbot import db

class User(db.Model):
    email = db.Column(db.String(30), primary_key=True)
    kakao_id = db.Column(db.String(10), nullable=False)
    name = db.Column(db.String(10), nullable=False)
    group = db.Column(db.String(20), nullable=False)
    usertype = db.Column(db.String(10), nullable=False)
    isbp = db.Column(db.Boolean(), server_default='0', nullable=False)

class Answer(db.Model):
    user = db.relationship('User', backref=db.backref('answer_set'))

    answer_id = db.Column(db.Integer, primary_key=True)
    kakao_id = db.Column(db.String(10),
                         db.ForeignKey('user.kakao_id',
                                       ondelete='CASCADE'),
                         nullable=False)
    checkdate = db.Column(db.Date(), nullable=True)
    checktime = db.Column(db.DateTime(), nullable=True)
    work_start_time = db.Column(db.String(10), nullable=True)
    work_end_time = db.Column(db.String(10), nullable=True)
    checkstatus = db.Column(db.String(10), nullable=False)
    workplace = db.Column(db.String(10), nullable=True)
    temperature = db.Column(db.Float, nullable=True)
    unusual = db.Column(db.Text(), nullable=True)
    
class Server(db.Model):
    date = db.Column(db.Date(), primary_key=True)
    status = db.Column(db.String(10), nullable=True)
    firstSend = db.Column(db.Boolean(), server_default='0')
    secondSend = db.Column(db.Boolean(), server_default='0')
    thirdSend = db.Column(db.Boolean(), server_default='0')
 