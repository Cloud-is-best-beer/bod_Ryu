from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

import config

db = SQLAlchemy()
migrate = Migrate()




def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # ORM
    db.init_app(app)

    # SQLite 오류해결(render_as_batch 가 False면 오류남)
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith("sqlite"):
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)
    
    from . import models

    # 블루프린트
    from .views import main_views, post_views, comment_views, auth_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(post_views.bp)
    app.register_blueprint(comment_views.bp)
    app.register_blueprint(auth_views.bp)

    # 날짜 필터
    from .filter import format_datetime
    app.jinja_env.filters['datetime'] = format_datetime

    return app
