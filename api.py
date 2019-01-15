from flask import Flask
from flask_restful import Api, Resource, reqparse
from datetime import datetime, date
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
api = Api(app)

app.config ['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://54.91.135.139:5432/helloworld'
db = SQLAlchemy(app)


class Database(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique= True)
    dateofBirth = db.Column(db.String(120))


    def __init__(self,username,dateofBirth):
        self.username = username
        self.dateofBirth = dateofBirth

class User(Resource):

    def put(self, name):

        parser = reqparse.RequestParser()
        parser.add_argument("dateofBirth")
        args = parser.parse_args()

        user = db.session.query(Database).filter(Database.username == name).first()

        if user is None:
            user = Database(name, args["dateofBirth"])
            db.session.add(user)
        else:
            user.dateofBirth = args["dateofBirth"]

        db.session.commit()

        return '',204


    def get(self, name):

        user = db.session.query(Database).filter(Database.username == name).first()

        birth = datetime.strptime(user.dateofBirth, "%Y-%m-%d").date()

        today = date.today()

        nextbirthday = date(today.year,birth.month,birth.day)

        result = (nextbirthday - today).days

        if (result < 0):
            nextbirthday = date(today.year+1,birth.month,birth.day)
            result = (nextbirthday - today).days

        if (result > 0):
            return {"message": "Hello "+user.username+"! Your birthday is in "+str(result)+" days"}

        elif (result == 0):
            return {"message": "Hello "+user.username+"! Happy Birtday!"}


if __name__ == "__main__":
    db.create_all()
    api.add_resource(User, "/hello/<string:name>")
    app.run(host='0.0.0.0')
