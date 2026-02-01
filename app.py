from flask import Flask, jsonify, request
import random
import threading
import time
from datetime import datetime, timedelta

app = Flask(__name__)

# ================= CONFIGURATION PRODUCTION =================
DUREE_CYCLE = 60 * 60       # 60 minutes
DUREE_FERMETURE = 5 * 60    # 5 minutes avant la fin

participants = []
gagnant = None
fin_inscription = None
etat = "ouvert"

# ================= LOGIQUE CYCLE =================
def nouveau_cycle():
    global participants, gagnant, fin_inscription, etat
    participants = []
    gagnant = None
    etat = "ouvert"
    fin_inscription = datetime.now() + timedelta(seconds=DUREE_CYCLE)
    print(f"🔁 Nouveau cycle démarré jusqu’à {fin_inscription}")

def gestion_cycle():
    global etat, gagnant

    while True:
        maintenant = datetime.now()

        if fin_inscription is None:
            time.sleep(1)
            continue

        # Fermeture automatique
        if etat == "ouvert" and maintenant >= fin_inscription - timedelta(seconds=DUREE_FERMETURE):
            etat = "fermé"
            print("🔒 Inscriptions fermées")

        # Tirage automatique à la fin
        if etat == "fermé" and gagnant is None and maintenant >= fin_inscription:
            if participants:
                gagnant = random.choice(participants)
                print(f"🎉 Gagnant : {gagnant}")
            else:
                print("⚠️ Aucun participant")

            # Pause courte avant nouveau cycle
            time.sleep(10)
            nouveau_cycle()

        time.sleep(1)

# ================= API =================
@app.route("/statut", methods=["GET"])
def statut():
    temps_restant = int((fin_inscription - datetime.now()).total_seconds())

    # Calcul dynamique de l'état
    if datetime.now() < fin_inscription - timedelta(seconds=DUREE_FERMETURE):
        current_etat = "ouvert"
    else:
        current_etat = "fermé"

    return jsonify({
        "etat": current_etat,
        "gagnant": gagnant,
        "temps_restant": max(0, temps_restant)
    })

@app.route("/participants", methods=["GET"])
def get_participants():
    return jsonify({"participants": participants})

@app.route("/participer", methods=["POST"])
def participer():
    if etat != "ouvert":
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
    nouveau_cycle()  # INITIALISATION
    threading.Thread(target=gestion_cycle, daemon=True).start()
    app.run(host="0.0.0.0", port=5000)
