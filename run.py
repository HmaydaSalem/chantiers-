from app import create_app

# Créer l'application et l'assigner à une variable nommée 'app'
app = create_app()

# Vercel n'a pas besoin de cette partie, mais vous pouvez la laisser pour le local
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
