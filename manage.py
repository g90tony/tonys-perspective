from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

from app import create_app

app = create_app('development')
manager = Manager(app)
server = Server('server', Server)

@manager.shell
def make_shell_context():
    return dict(app = app)

if __name__ == '__main__':
    manager.run()