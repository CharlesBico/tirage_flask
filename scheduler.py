from datetime import datetime, timedelta
import random
from models import db, Participant, Tirage

def executer_tirage():
    now = datetime.now().replace(minute=0, second=0, microsecond=0)

    tirage = Tirage.query.filter_by(heure=now).first()
    if not tirage:
        return

    if tirage.etat == "termine":
        return

    participants = Participant.query.filter_by(heure_tirage=now).all()

    if participants:
        gagnant = random.choice(participants)
        tirage.gagnant = gagnant.nom
    else:
        tirage.gagnant = None

    tirage.etat = "termine"
    db.session.commit()
