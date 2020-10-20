from app import create_app
from flask_script import Manager,Server

app = create_app('development')

manager = Manager(app)
manager.add_command('server', Server)

if _name_ == '_main_':
    manager.run()