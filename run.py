from app import create_app

# Création de l'application Flask
app = create_app()

# Vercel utilise cette variable 'app' pour lancer votre site
if __name__ == "__main__":
    @app.route('/test')
def test():
    return "Ça marche !"
    app.run()
