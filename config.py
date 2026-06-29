import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
INSTANCE_DIR = os.path.join(BASE_DIR, "instance")


class Config:
    """Configuration de base. Surcharger via variables d'environnement en production."""

    SECRET_KEY = os.environ.get("SECRET_KEY", "a-changer-absolument-en-production")

    # IMPORTANT : chemin ABSOLU pour la base de données.
    # (cf. le souci rencontré avec StoreManager où un chemin relatif posait
    # problème selon l'endroit d'où l'app était lancée — exe vs PythonAnywhere)
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(
        INSTANCE_DIR, "chantier_manager.db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Dossier où sont stockées les photos de chantier uploadées
    UPLOAD_FOLDER = os.path.join(INSTANCE_DIR, "uploads")
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 Mo max par upload (photos chantier)
