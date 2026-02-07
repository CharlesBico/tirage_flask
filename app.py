from flask import Flask, jsonify, request
import random
import time

app = Flask(__name__)

# =========================
# CONFIGURATION
# =========================
DUREE_OUVERT = 600   # 10 minutes
DUREE_FERME = 60    # 1 minute

etat = "ouvert"
debut_phase = time.time()
participants = []
gagnant = None

# =========================
# LOGIQUE CENTRALE (CRITIQUE)
# =========================
def update_etat():
    global etat, debut_phase, gagnant, participants

    now = time.time()
    elapsed = int(now - debut_phase)

    if etat == "ouvert" and elapsed >= DUREE_OUVERT:
        # Tirage du gagnant
        gagnant = random.choice(participants) if participants else None
        etat = "fermé"
        debut_phase = now

    elif etat == "fermé" and elapsed >= DUREE_FERME:
        # Nouveau cycle
        etat = "ouvert"
        debut_phase = now
        gagnant = None
        participants.clear()

# =========================
# ENDPOINTS
# =========================
@app.route("/statut")
def statut():
    update_etat()

    now = time.time()
    elapsed = int(now - debut_phase)

    if etat == "ouvert":
        temps_restant = max(0, DUREE_OUVERT - elapsed)
    else:
        temps_restant = max(0, DUREE_FERME - elapsed)

    return jsonify({
        "etat": etat,
        "gagnant": gagnant,
        "temps_restant": temps_restant
    })

@app.route("/participants")
def get_participants():
    return jsonify({"participants": participants})

@app.route("/participer", methods=["POST"])
def participer():
    update_etat()

    data = request.get_json()
    nom = data.get("nom")

    if etat != "ouvert":
        return jsonify({"error": "Participation fermée"}), 400

    if not nom:
        return jsonify({"error": "Nom invalide"}), 400

    participants.append(nom)
    return jsonify({"success": True})

# =========================
# MAIN
# =========================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
