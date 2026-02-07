from flask import Flask, jsonify, request
import random
import time
from threading import Thread

app = Flask(__name__)

# =========================
# CONFIGURATION
# =========================
DUREE_OUVERT = 600   # 10 min
DUREE_TIRAGE = 60    # 1 min
DUREE_FERME = 60     # 1 min après tirage pour afficher gagnant

etat = "fermé"
participants = []
gagnant = None
fin_ouvert = 0
fin_tirage = 0

# =========================
# LOGIQUE CYCLE
# =========================
def cycle_automatique():
    global etat, participants, gagnant, fin_ouvert, fin_tirage

    while True:
        # --- OUVERT ---
        etat = "ouvert"
        participants.clear()
        gagnant = None
        fin_ouvert = time.time() + DUREE_OUVERT
        while time.time() < fin_ouvert:
            time.sleep(1)

        # --- TIRAGE ---
        etat = "tirage"
        fin_tirage = time.time() + DUREE_TIRAGE
        while time.time() < fin_tirage:
            time.sleep(1)

        # --- FERMÉ et tirage du gagnant ---
        etat = "fermé"
        if participants:
            gagnant = random.choice(list(set(participants)))  # supprime doublons
        else:
            gagnant = None

        # pause pour afficher le gagnant avant de repartir
        time.sleep(DUREE_FERME)

# Thread pour exécuter le cycle automatiquement
thread = Thread(target=cycle_automatique, daemon=True)
thread.start()

# =========================
# ENDPOINTS
# =========================
@app.route("/statut")
def get_statut():
    if etat == "ouvert":
        temps_restants = max(int(fin_ouvert - time.time()), 0)
    elif etat == "tirage":
        temps_restants = max(int(fin_tirage - time.time()), 0)
    else:
        temps_restants = 0

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
