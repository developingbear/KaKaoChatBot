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

    return app

def print_some():
    print(datetime.now().time())
     


