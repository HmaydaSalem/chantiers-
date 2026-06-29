import os

class Config:
    # 1. Clé secrète (Indispensable pour Flask-Login et les formulaires)
    # Utilisez une valeur par défaut sûre pour Vercel, 
    # vous pourrez la définir dans les "Environment Variables" de Vercel plus tard.
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'une-cle-secrete-tres-difficile-a-deviner'

    # 2. Configuration corrigée pour la base de données
    # Sur Vercel, on utilise la mémoire vive, sinon on cherche une variable d'environnement
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///:memory:'
    
    # 3. Désactiver le suivi des modifications pour économiser des ressources
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 4. Autres paramètres utiles
    DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# Pour vérifier que tout est bien configuré lors du chargement
if __name__ == "__main__":
    print(f"Base de données configurée sur : {Config.SQLALCHEMY_DATABASE_URI}")
