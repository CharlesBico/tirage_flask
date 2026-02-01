from flask import Flask, jsonify, request
import random
import threading
import time
from datetime import datetime, timedelta

app = Flask(__name__)

# ================= CONFIGURATION =================
DUREE_CYCLE = 2 * 60        # 60 minutes
DUREE_FERMETURE = 10     # 5 minutes avant la fin

participants = []
gagnant = None
fin_inscription = None

# ================= LOGIQUE CYCLE =================
def nouveau_cycle():
    """Démarre un nouveau cycle d'inscription"""
    global participants, gagnant, fin_inscription
    participants = []
    gagnant = None
    fin_inscription = datetime.now() + timedelta(seconds=DUREE_CYCLE)
    print(f"🔁 Nouveau cycle démarré jusqu’à {fin_inscription}")

def gestion_cycle():
    """Thread pour gérer la fermeture et le tirage automatique"""
    global gagnant
    while True:
        maintenant = datetime.now()
        if fin_inscription is None:
            time.sleep(1)
            continue

        temps_restant = (fin_inscription - maintenant).total_seconds()

        # Tirage automatique à la fin
        if temps_restant <= 0 and gagnant is None:
            if participants:
                gagnant = random.choice(participants)
                print(f"🎉 Gagnant : {gagnant}")
            else:
                print("⚠️ Aucun participant")
            time.sleep(5)
            nouveau_cycle()

        time.sleep(1)

# ================= API =================
@app.route("/statut", methods=["GET"])
def statut():
    maintenant = datetime.now()
    if fin_inscription is None:
        temps_restant = 0
    else:
        temps_restant = int((fin_inscription - maintenant).total_seconds())

    # Calcul dynamique de l'état
    if temps_restant > DUREE_FERMETURE:
        etat_calcule = "ouvert"
    else:
        etat_calcule = "fermé"

    return jsonify({
        "etat": etat_calcule,
        "gagnant": gagnant,
        "temps_restant": max(0, temps_restant)
    })

@app.route("/participants", methods=["GET"])
def get_participants():
    return jsonify({"participants": participants})

@app.route("/participer", methods=["POST"])
def participer():
    maintenant = datetime.now()
    temps_restant = (fin_inscription - maintenant).total_seconds()

    # Inscriptions fermées si moins que DUREE_FERMETURE
    if temps_restant <= DUREE_FERMETURE:
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
    nouveau_cycle()  # Initialisation
    threading.Thread(target=gestion_cycle, daemon=True).start()
    app.run(host="0.0.0.0", port=5000)
