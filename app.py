from flask import Flask
import config
from exts import db
from models import User,Sample,Facility,Beamline,Group,DivideGroup,Spectra
from blueprints.auth import bp as auth_bp
from flask_migrate import Migrate

app = Flask(__name__)
# 绑定配置文件
app.config.from_object(config)

db.init_app(app)

migrate = Migrate(app, db)

app.register_blueprint(auth_bp)

if __name__ == '__main__':
    app.run()
