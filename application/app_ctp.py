from flask import Flask, render_template, request, redirect, url_for
from google.cloud import storage
import os
import json
from uuid import uuid4
import sys

app = Flask(__name__)

# Configurer le bucket Cloud Storage
BUCKET_NAME = os.getenv("BUCKET_NAME")
if not BUCKET_NAME: 
    print(" Erreur : La variable d'environnement 'BUCKET_NAME' n'est pas définie.", file=sys.stderr) 
    sys.exit(1)  # Arrête le programme avec un code d'erreur

def get_storage_client():
    """Initialise le client Google Cloud Storage."""
    return storage.Client()

@app.route('/app/<name>')
def afficherLien(World):
return f'Hello {name}'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
