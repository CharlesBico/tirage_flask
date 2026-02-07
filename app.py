from flask import Flask, jsonify, request
import random
import time
from threading import Thread, Lock

app = Flask(__name__)

# =========================
# CONFIGURATION
# =========================
DUREE_OUVERT = 600  # 10 min
DUREE_FERME = 60    # 1 min

etat = "fermé"
participants = set()
gagnant = None

fin_ouvert = 0
fin_ferme = 0

lock = Lock()

# =========================
# CYCLE AUTOMATIQUE
# =========================
def cycle_automatique():
    global etat, participants, gagnant, fin_ouvert, fin_ferme

    while True:
        # ---- Phase ouverte ----
        with lock:
            etat = "ouvert"
            participants.clear()
            gagnant = None
            fin_ouvert = time.time() + DUREE_OUVERT
            fin_ferme = 0

        while time.time() < fin_ouvert:
            time.sleep(1)

        # ---- Phase fermée / tirage ----
        with lock:
            etat = "fermé"
            if participants:
                gagnant = random.choice(list(participants))
            else:
                gagnant = None
            fin_ferme = time.time() + DUREE_FERME
            fin_ouvert = 0

        while time.time() < fin_ferme:
            time.sleep(1)

# Thread daemon
Thread(target=cycle_automatique, daemon=True).start()

# =========================
# ENDPOINTS
# =========================
@app.route("/statut")
def get_statut():
    with lock:
        if etat == "ouvert":
            temps_restant = max(int(fin_ouvert - time.time()), 0)
        elif etat == "fermé":
            temps_restant = max(int(fin_ferme - time.time()), 0)
        else:
            temps_restant = 0

        return jsonify({
            "etat": etat,
            "gagnant": gagnant,
            "temps_restant": temps_restant
        })

@app.route("/participants")
def get_participants():
    with lock:
        return jsonify({"participants": sorted(list(participants))})

@app.route("/participer", methods=["POST"])
def add_participant():
    with lock:
        if etat != "ouvert":
            return jsonify({"error": "Tirage fermé"}), 400

        data = request.get_json()
        nom = data.get("nom", "").strip()
        if not nom:
            return jsonify({"error": "Nom invalide"}), 400

        participants.add(nom)  # pas de doublons
        return jsonify({"success": True})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
