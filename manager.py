# -*- encoding: utf-8 -*-
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import create_app
from app.models import db

monitor_app = create_app('development')

migrate = Migrate(monitor_app, db)

manager = Manager(app=monitor_app)

manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()
