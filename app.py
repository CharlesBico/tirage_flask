from flask import Flask, jsonify, request
import random
import time

app = Flask(__name__)

# ================= CONFIG =================
DUREE_OUVERT = 600   # 10 minutes
DUREE_FERME = 60     # 1 minute

etat = "ouvert"
participants = []
gagnant = None
fin_phase = time.time() + DUREE_OUVERT


# ================= LOGIQUE TEMPS =================
def update_cycle():
    global etat, participants, gagnant, fin_phase

    now = time.time()

    if now < fin_phase:
        return

    # 🔁 PHASE TERMINÉE
    if etat == "ouvert":
        # ➜ on ferme + tirage
        etat = "fermé"
        gagnant = random.choice(participants) if participants else None
        fin_phase = now + DUREE_FERME

    else:
        # ➜ on rouvre
        etat = "ouvert"
        participants.clear()
        gagnant = None
        fin_phase = now + DUREE_OUVERT


# ================= ENDPOINTS =================
@app.route("/statut")
def statut():
    update_cycle()

    temps = max(int(fin_phase - time.time()), 0)

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
    update_cycle()

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
