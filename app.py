from flask import Flask, jsonify, request
import random
import time
from threading import Thread

app = Flask(__name__)

# =========================
# CONFIGURATION
# =========================
DUREE_OUVERT = 600   # 10 min
DUREE_FERME = 60     # 1 min

etat = "fermé"
participants = []
gagnant = None
fin_cycle = time.time()  # timestamp de fin du cycle

# =========================
# LOGIQUE CYCLE
# =========================
def cycle_automatique():
    global etat, participants, gagnant, fin_cycle
    while True:
        etat = "ouvert"
        participants.clear()
        gagnant = None
        fin_cycle = time.time() + DUREE_OUVERT
        time.sleep(DUREE_OUVERT)

        etat = "fermé"
        if participants:
            gagnant = random.choice(participants)
        else:
            gagnant = None
        fin_cycle = time.time() + DUREE_FERME
        time.sleep(DUREE_FERME)

# Thread pour exécuter le cycle automatiquement
thread = Thread(target=cycle_automatique, daemon=True)
thread.start()

# =========================
# ENDPOINTS
# =========================
@app.route("/statut")
def get_statut():
    temps_restants = max(int(fin_cycle - time.time()), 0)
    return jsonify({
        "etat": etat,
        "gagnant": gagnant,
        "temps_restant": temps_restants
    })

@app.route("/participants")
def get_participants():
    return jsonify({"participants": participants})

@app.route("/participer", methods=["POST"])
def add_participant():
    data = request.get_json()
    nom = data.get("nom")
    if nom and etat == "ouvert":
        participants.append(nom)
        return jsonify({"success": True})
    return jsonify({"error": "Participation fermée"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
