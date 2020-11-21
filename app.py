from flask import Flask, jsonify, request
from  flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app = Flask(__name__)
db = SQLAlchemy(app)
ma = Marshmallow(app)

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
    return vip_schema.jsonify(new_vip)
    # return jsonify({"msg": "A new VIP has been added to our database"})

class VIPSchema(ma.Schema):
    class Meta:
        fields = ("id", "first_name", "last_name")

vip_schema = VIPSchema()
vips_schema = VIPSchema(many=True)

@app.route("/hollywood", methods = ["GET"])
def get_vips():
    vips = VIP.query.all()
    outcome = vips_schema.dump(vips)
    return jsonify(outcome)


@app.route("/delete-<int:id>", methods = ["DELETE"])
def delete_vips(id):
    id = VIP.query.get(id)
    db.session.delete(id)
    db.session.commit()
    return jsonify({"msg": "The VIP has been deleted"})

@app.route("/update-<int:id>", methods = ["PUT"])
def update_vips(id):
    vip_person = VIP.query.get(id)
    body = request.get_json()
    vip_person.first_name = body["first_name"]
    vip_person.last_name = body["last_name"]
    db.session.commit()
    return vip_schema.jsonify(vip_person)






if __name__=="__main__":
    app.run(debug=True)
