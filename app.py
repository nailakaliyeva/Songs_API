from flask import Flask, jsonify, request, render_template
from  flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
db = SQLAlchemy(app)
ma = Marshmallow(app)

app.config["SQLALCHEMY_DATABASE_URI"]= "sqlite:///site.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= False

@app.route("/")
def greeting():
    return render_template("index.html")

class Vip(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(250), nullable = False)
    last_name = db.Column(db.String(250))
    zodiac_sign = db.Column(db.String(12))
    ethnicity = db.Column(db.String(250))
    religion = db.Column(db.String(250))
    race = db.Column(db.String(100))
    songs = db.relationship("Song", backref = "singer", lazy="dynamic")
    def __init__(self, first_name, last_name, zodiac_sign, ethnicity, religion, race):
        self.first_name = first_name
        self.last_name = last_name
        self.zodiac_sign = zodiac_sign
        self.ethnicity = ethnicity
        self.religion = religion
        self.race = race


class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    song_name = db.Column(db.String(250), nullable = False)
    date_released = db.Column(db.String(250))
    album = db.Column(db.String(250))
    lyrics = db.Column(db.Text)
    singer_id = db.Column(db.Integer, db.ForeignKey("vip.id"))
    def __init__(self, song_name, date_released, album, lyrics, singer_id):
        self.song_name = song_name
        self.date_released = date_released
        self.album = album
        self.lyrics = lyrics
        self.singer_id = singer_id

@app.route("/singers", methods = ["POST"])
def post_vip():
    body = request.get_json()
    first_name = body["first_name"]
    last_name = body["last_name"]
    zodiac_sign =  body["zodiac_sign"]
    ethnicity =  body["ethnicity"]
    religion =  body["religion"]
    race =  body["race"]
    new_vip = Vip(first_name = first_name, last_name = last_name, zodiac_sign = zodiac_sign, ethnicity = ethnicity, religion=religion, race=race)
    db.session.add(new_vip)
    db.session.commit()
    return vip_schema.jsonify(new_vip)

@app.route("/songs", methods = ["POST"])
def post_song():
    body = request.get_json()
    song_name = body["song_name"]
    date_released = body["date_released"]
    album = body["album"]
    lyrics =body["lyrics"]
    singer_id = body["singer_id"]
    new_song = Song(song_name, date_released, album, lyrics, singer_id)
    db.session.add(new_song)
    db.session.commit()
    return song_schema.jsonify(new_song)

class VipSchema(ma.Schema):
    class Meta:
        fields = ("id", "first_name", "last_name", "zodiac_sign", "ethnicity", "religion", "race")
vip_schema = VipSchema()
vips_schema = VipSchema(many=True)

class SongSchema(ma.Schema):
    class Meta:
        fields = ("id", "song_name", "date_released", "album", "lyrics", "singer_id")
song_schema = SongSchema()
songs_schema = SongSchema(many=True)

@app.route("/singers", methods = ["GET"])
def get_vips():
    vips = Vip.query.all()
    outcome = vips_schema.dump(vips)
    return jsonify(outcome)

@app.route("/songs", methods = ["GET"])
def get_songs():
    songs = Song.query.all()
    outcome = songs_schema.dump(songs)
    return jsonify(outcome)


@app.route("/singers/delete-<int:id>", methods = ["DELETE"])
def delete_vips(id):
    id = Vip.query.get(id)
    db.session.delete(id)
    db.session.commit()
    return jsonify({"msg": "The singer has been deleted"})

@app.route("/songs/delete-<int:id>", methods = ["DELETE"])
def delete_songss(id):
    id = Song.query.get(id)
    db.session.delete(id)
    db.session.commit()
    return jsonify({"msg": "The song has been deleted"})

@app.route("/singers/update-<int:id>", methods = ["PUT"])
def update_vips(id):
    vip_person = Vip.query.get(id)
    body = request.get_json()
    vip_person.first_name = body["first_name"]
    vip_person.last_name = body["last_name"]
    vip_person.zodiac_sign = body["zodiac_sign"]
    vip_person.ethnicity = body["ethnicity"]
    vip_person.religion = body["religion"]
    vip_person.race = body["race"]
    vip_person.songs = body["songs"]
    db.session.commit()
    return vip_schema.jsonify(vip_person)

@app.route("/songs/update-<int:id>", methods = ["PUT"])
def update_songs(id):
    the_song= Song.query.get(id)
    body = request.get_json()
    the_song.song_name = body["song_name"]
    the_song.date_released = body["date_released"]
    the_song.album = body["album"]
    the_song.lyrics =body["lyrics"]
    the_song.singer_id = body["singer_id"]
    db.session.commit()
    return song_schema.jsonify(the_song)


if __name__=="__main__":
    app.run(debug=True)
