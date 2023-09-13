from flask import Flask
from connector import ConnectorDatabase
from repository import Repository
from controller import Routes

if __name__ == '__main__':
    app = Flask(__name__)

    connector = ConnectorDatabase(
        host='localhost',
        user='root',
        password='root',
        database='student',
        port=int(3307)
    )
    repository = Repository(connector)

    routes = Routes(app, repository)

    app.run(host='0.0.0.0', port=8080)