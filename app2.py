import os
from flask import Flask
from flask_sqlalchemy import  SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))  # 내 현재경로
dbfile = os.path.join(basedir, "db.sqlite")     # 데이터베이스 경로

print(basedir)
print(dbfile)

app = Flask(__name__)

app.config['SQLAlCHEMY_DATABASE_URI'] = 'sqlite:///'+dbfile
app.config['SQLAlCHEMY_COMMIT_ON_TEARDOWN'] = True      # 누군가가 정보를 요청하면 커밋을 하겠다.
app.config['SQLAlCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Test(db.Model):
    __tablename__ = 'test_table'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(32), unique = True)

db.create_all()

@app.route('/')
def hello():
    return 'Hello World!'