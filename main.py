from data import db_session, news_api
from data.work import User
from data.jobs import Jobs
import datetime as dt
from flask import Flask

app = Flask(__name__)


def main():
    db_session.global_init("db/blogs.db")
    app.register_blueprint(news_api.blueprint)
    app.run()


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
