from app import create_app, db
from app.models import Subscribers
from flask_script import Manager, Shell


app = create_app('basic')
manager = Manager(app)


def make_shell_context():
    return dict(app=app, db=db, Subscribers=Subscribers)


manager.add_command("shell", Shell(make_context=make_shell_context))


if __name__ == '__main__':
    manager.run()
