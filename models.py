from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Participant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), unique=True, nullable=False)
    heure_tirage = db.Column(db.DateTime, nullable=False)

class Tirage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    heure = db.Column(db.DateTime, unique=True, nullable=False)
    gagnant = db.Column(db.String(100))
    etat = db.Column(db.String(20), default="ouvert")  # ouvert | bloque | termine
