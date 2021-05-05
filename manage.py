from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

from app import create_app, db
from app.models import User, Article, Category, Comment, Quote

app = create_app('development')

manager = Manager(app)
migrate= Migrate(app, db)


manager.add_command('db', MigrateCommand)
manager.add_command('server', Server)

@manager.shell
def make_shell_context():
    return dict(app = app, db = db, User= User, Article= Article, Category= Category, Comment= Comment, Quote= Quote)

if __name__ == '__main__':
    manager.run()