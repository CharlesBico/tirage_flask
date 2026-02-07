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

etat = "fermé"        # ouvert / tirage / fermé
participants = []
gagnant = None
fin_cycle = time.time()

# =========================
# LOGIQUE CYCLE
# =========================
def cycle_automatique():
    global etat, participants, gagnant, fin_cycle
    while True:
        # --- Phase ouverte ---
        etat = "ouvert"
        participants.clear()
        gagnant = None
        fin_cycle = time.time() + DUREE_OUVERT
        time.sleep(DUREE_OUVERT)

        # --- Phase tirage ---
        etat = "tirage"
        fin_cycle = time.time() + DUREE_TIRAGE
        time.sleep(DUREE_TIRAGE)

        # --- Phase fermée / gagnant ---
        etat = "fermé"
        gagnant = random.choice(participants) if participants else None
        fin_cycle = time.time() + 5  # court délai avant la prochaine ouverture
        time.sleep(5)

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
        if nom not in participants:  # interdiction des doublons
            participants.append(nom)
            return jsonify({"success": True})
        return jsonify({"error": "Nom déjà ajouté"}), 400
    return jsonify({"error": "Participation fermée"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
