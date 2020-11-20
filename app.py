from flask import Flask, jsonify, request
from  flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

app.config["SQLALCHEMY_DATABASE_URI"]= "sqlite:///site.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= False

@app.route("/")
def greeting():
    return jsonify({"msg": "Hello, this is a greeting page"})


class VIP(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(250), nullable = False)
    last_name = db.Column(db.String(250))

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

@app.route("/hollywood", methods = ["POST"])
def post_vip():
    body = request.get_json()
    first_name = body["first_name"]
    last_name = body["last_name"]
    new_vip = VIP(first_name, last_name)
    db.session.add(new_vip)
    db.session.commit()
    return jsonify({"msg": "A new VIP has been added to our database"})

@app.route("/hollywood", methods = ["GET"])
def get_vips():
    vips = VIP.query.all()
    for vip in vips:
        return jsonify(vip)







if __name__=="__main__":
    app.run(debug=True)
