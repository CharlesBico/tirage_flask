from flask import Flask, jsonify, request
import random
import time
from threading import Thread, Lock

app = Flask(__name__)

# =========================
# CONFIGURATION
# =========================
DUREE_OUVERT = 600   # 10 minutes
DUREE_FERME = 60     # 1 minute

etat = "fermé"
participants = set()   # ✅ set = pas de doublons
gagnant = None
fin_cycle = 0

lock = Lock()

# =========================
# CYCLE AUTOMATIQUE
# =========================
def cycle_automatique():
    global etat, gagnant, fin_cycle, participants

    while True:
        # 🔓 PHASE OUVERTE
        with lock:
            etat = "ouvert"
            participants.clear()
            gagnant = None
            fin_cycle = time.time() + DUREE_OUVERT

        while time.time() < fin_cycle:
            time.sleep(1)

        # 🔒 PHASE FERMÉE (TIRAGE)
        with lock:
            etat = "fermé"
            if participants:
                gagnant = random.choice(list(participants))
            else:
                gagnant = None
            fin_cycle = time.time() + DUREE_FERME

        while time.time() < fin_cycle:
            time.sleep(1)

# =========================
# THREAD
# =========================
Thread(target=cycle_automatique, daemon=True).start()

# =========================
# ENDPOINTS
# =========================
@app.route("/statut")
def statut():
    with lock:
        temps_restant = max(int(fin_cycle - time.time()), 0)
        return jsonify({
            "etat": etat,
            "gagnant": gagnant,
            "temps_restant": temps_restant
        })

@app.route("/participants")
def liste_participants():
    with lock:
        return jsonify({
            "participants": sorted(list(participants))
        })

@app.route("/participer", methods=["POST"])
def participer():
    with lock:
        if etat != "ouvert":
            return jsonify({"error": "Tirage fermé"}), 400

        data = request.get_json()
        nom = data.get("nom", "").strip()

        if not nom:
            return jsonify({"error": "Nom invalide"}), 400

        participants.add(nom)  # ✅ pas de doublons
        return jsonify({"success": True})

# =========================
# MAIN
# =========================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
