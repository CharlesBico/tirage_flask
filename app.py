from flask import Flask, jsonify, request
import random
import time
from threading import Thread

app = Flask(__name__)

# ================= CONFIG =================
DUREE_OUVERT = 600
DUREE_FERME = 60

etat = "ouvert"
participants = []
gagnant = None
fin_cycle = time.time() + DUREE_OUVERT

# ================= CYCLE TEMPS REEL =================
def cycle():
    global etat, participants, gagnant, fin_cycle

    while True:

        # PHASE OUVERTE
        etat = "ouvert"
        participants.clear()
        gagnant = None
        fin_cycle = time.time() + DUREE_OUVERT

        time.sleep(DUREE_OUVERT)

        # PHASE FERMEE + TIRAGE
        etat = "fermé"

        if participants:
            gagnant = random.choice(participants)
        else:
            gagnant = None

        fin_cycle = time.time() + DUREE_FERME

        time.sleep(DUREE_FERME)

# Lancement thread
Thread(target=cycle, daemon=True).start()

# ================= ENDPOINTS =================
@app.route("/statut")
def statut():
    temps = max(int(fin_cycle - time.time()), 0)

    return jsonify({
        "etat": etat,
        "gagnant": gagnant,
        "temps_restant": temps
    })


@app.route("/participants")
def get_participants():
    return jsonify({"participants": participants})


@app.route("/participer", methods=["POST"])
def participer():

    if etat != "ouvert":
        return jsonify({"error": "Participation fermée"}), 400

    data = request.get_json()
    nom = data.get("nom")

    if nom:
        participants.append(nom)
        return jsonify({"success": True})

    return jsonify({"error": "Nom invalide"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
