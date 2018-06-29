from flask import Flask
from flask_script import Manager, Server
from flask_migrate import MigrateCommand
from app import create_app

app = create_app('dev')
manager = Manager(app)
manager.add_command('start', Server(host='127.0.0.1', port=9000))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
