from flask import Flask
#DB 관련
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import config
db = SQLAlchemy()
migrate = Migrate()
#model 관련
from . import models
from datetime import datetime
 
def create_app():
    app = Flask(__name__)
    #DB config
    app.config.from_object(config)
    #ORM
    db.init_app(app)
    migrate.init_app(app, db)
    
    #Blueprint
    from .views import main_views
    app.register_blueprint(main_views.bp)
    
    #timer
    from apscheduler.schedulers.background import BackgroundScheduler
    from chatbot.control.commands.init import Init
    scheduler = BackgroundScheduler(daemon=True)
    scheduler.add_job(Init.DBtoday, 'cron', hour = 0, minute = 0, second=1) 
    scheduler.start()

    return app

""" 
http://kakaochatbot-wpvdo.run.goorm.io/check/%7B%22id%22:%22ons문창주%22,%22msg%22:%22del%22%7D
"""

