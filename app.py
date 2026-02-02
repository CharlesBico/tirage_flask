from flask import Flask, jsonify, request
import random
from datetime import datetime, timedelta

app = Flask(__name__)

# ================= CONFIG =================
DUREE_CYCLE = 10 * 60       # 60 minutes
DUREE_FERMETURE = 1 * 60    # 5 minutes avant tirage

# ================= STOCKAGE =================
participants = []
gagnant = None
fin_inscription = datetime.now() + timedelta(seconds=DUREE_CYCLE)

# ================= FONCTIONS =================
def get_etat():
    """Retourne 'ouvert' ou 'fermé' selon le temps"""
    now = datetime.now()
    if now < fin_inscription - timedelta(seconds=DUREE_FERMETURE):
        return "ouvert"
    else:
        return "fermé"

def calculer_gagnant():
    """Retourne le gagnant si tirage fait, sinon None"""
    global gagnant, participants, fin_inscription
    now = datetime.now()
    if now >= fin_inscription:
        if gagnant is None and participants:
            gagnant = random.choice(participants)
        # Nouveau cycle automatique si le temps est écoulé
        if now >= fin_inscription + timedelta(seconds=10):
            participants = []
            gagnant = None
            fin_inscription = datetime.now() + timedelta(seconds=DUREE_CYCLE)
            print("🔁 Nouveau cycle démarré jusqu’à", fin_inscription)
    return gagnant

def temps_restant():
    """Retourne le temps restant en secondes pour le cycle"""
    delta = fin_inscription - datetime.now()
    return max(0, int(delta.total_seconds()))

# ================= API =================
@app.route("/statut", methods=["GET"])
def statut():
    return jsonify({
        "etat": get_etat(),
        "gagnant": calculer_gagnant(),
        "temps_restant": temps_restant()
    })

@app.route("/participants", methods=["GET"])
def get_participants():
    return jsonify({"participants": participants})

@app.route("/participer", methods=["POST"])
def participer():
    if get_etat() != "ouvert":
        return jsonify({"error": "Inscriptions fermées"}), 400

    data = request.get_json()
    nom = data.get("nom", "").strip()
    if not nom:
        return jsonify({"error": "Nom requis"}), 400

    if nom in participants:
        return jsonify({"error": "Nom déjà enregistré"}), 400

    participants.append(nom)
    return jsonify({"message": "OK"}), 200

# ================= DÉMARRAGE =================
if __name__ == "__main__":
    print("🔁 Serveur démarré, cycle initial jusqu’à", fin_inscription)
    app.run(host="0.0.0.0", port=5000)
