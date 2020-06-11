#приложение
from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

app = Flask(__name__)
app.config.from_object(Configuration)

db = SQLAlchemy(app)

# app и db потому что миграция выстраивает корреляцию межлу текущей версией приложения и базы данных
migrate = Migrate(app, db)

manager = Manager(app)
# 1-название команды, 2-что за комманда
manager.add_command('db', MigrateCommand)
