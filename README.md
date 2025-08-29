# mqtt-tg

Application de récupération et d’affichage de données capteurs via MQTT + stockage en base MongoDB + affichage web avec FastAPI.

## Fonctionnalités

- Connexion à un broker MQTT (The Things Network)
- Décodage des messages reçus (JSON)
- Stockage des données utiles dans une base MongoDB
- Affichage des mesures dans un tableau HTML Bootstrap
- Utilisation de fichiers `.env` pour sécuriser les infos de connexion
- API accessible via FastAPI avec documentation automatique Swagger

## Installation

### 1. Cloner le dépôt

```bash
git clone https://github.com/votre-utilisateur/mqtt-tg.git
cd mqtt-tg
```

### 2. Créer et activer un environnement virtuel

```bash
python -m venv .venv
.venv\Scripts\activate  # sous Windows
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Créer un fichier `.env` à la racine

> Ce fichier contient les identifiants pour MongoDB et MQTT. Il **ne doit pas être versionné**.

Exemple de contenu :
```env
DB_URI=mongodb://localhost:27017
DB_DATABASE=iot
DB_COLLECTION=mesures

MQTT_HOST=eu1.cloud.thethings.network
MQTT_USER=votre_identifiant
MQTT_PASSWORD=motdepasse
MQTT_SUBSCRIBE=votre/sujet/ttn/#
```

## Lancement

### 1. Lancer la récupération MQTT (exécution continue)

```bash
python getMsg.py
```

### 2. Lancer le serveur web FastAPI

```bash
fastapi dev main.py
```

Puis accéder à : [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Structure du projet

- `getMsg.py` : abonnement au broker MQTT, réception des messages, stockage MongoDB
- `main.py` : serveur FastAPI affichant les mesures dans un template HTML
- `webhook.py` : envoi des messages vers Discord (exercice complémentaire)
- `database.py` : connexion sécurisée à MongoDB
- `/templates/index.html` : tableau des mesures (Bootstrap)
- `.env` : variables d’environnement (non versionné)

## Fichiers non nécessaires à l’app principale

Certains fichiers étaient liés à des exercices complémentaires (par exemple Discord), mais ne sont pas indispensables pour le fonctionnement de l’appli :

- `webhook.py`
- `static/` (non utilisé ici)

## Documentation Swagger

Une doc interactive est disponible automatiquement :
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## Projet validé pour les objectifs suivants :
- Connexion MQTT
- Décodage JSON
- Stockage MongoDB
- Rendu HTML avec FastAPI
- Sécurisation avec `.env`