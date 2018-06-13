# -*- encoding: utf-8 -*-
from flask_script import Manager, Server
import main
import models


manager = Manager(main.app)


manager.add_command("server", Server())


@manager.shell
def make_shell_context():
    """Create a python CLI
       
       return Default import object
       type: dict
    """
    return dict(app=main.app,
                db=models.db,
                User=models.User,
                Post=models.Post,
                Comment=models.Comment)


if __name__ == "__main__":
    manager.run()
