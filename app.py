from flask import Flask, jsonify, request
import random
import threading
import time
from datetime import datetime, timedelta

app = Flask(__name__)

# Durées (en secondes)
DUREE_CYCLE = 10 * 60       # 60 minutes
DUREE_FERMETURE = 5 * 60   # 5 minutes avant la fin

participants = []
gagnant = None
etat = "ouvert"
fin_inscription = None


def nouveau_cycle():
    global participants, gagnant, etat, fin_inscription
    participants = []
    gagnant = None
    etat = "ouvert"
    fin_inscription = datetime.now() + timedelta(seconds=DUREE_CYCLE)
    print("🔁 Nouveau cycle démarré")


def gestion_tirage():
    global etat, gagnant

    while True:
        maintenant = datetime.now()

        # Sécurité : si pas encore initialisé
        if fin_inscription is None:
            time.sleep(1)
            continue

        # Fermer inscriptions à -5 min
        if etat == "ouvert" and maintenant >= fin_inscription - timedelta(seconds=DUREE_FERMETURE):
            etat = "fermé"
            print("🔒 Inscriptions fermées")

        # Tirage automatique à 0
        if etat == "fermé" and gagnant is None and maintenant >= fin_inscription:
            if participants:
                gagnant = random.choice(participants)
                print(f"🎉 Gagnant : {gagnant}")
            else:
                print("⚠️ Aucun participant")

            # Pause courte puis redémarrage
            time.sleep(10)
            nouveau_cycle()

        time.sleep(1)


@app.route("/statut", methods=["GET"])
def statut():
    temps_restant = int((fin_inscription - datetime.now()).total_seconds())
    return jsonify({
        "etat": etat,
        "gagnant": gagnant,
        "temps_restant": max(0, temps_restant)
    })


@app.route("/participants", methods=["GET"])
def participants_route():
    return jsonify(participants)


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


if __name__ == "__main__":
    nouveau_cycle()  # ✅ INITIALISATION OBLIGATOIRE
    threading.Thread(target=gestion_tirage, daemon=True).start()
    app.run(host="0.0.0.0", port=5000)
