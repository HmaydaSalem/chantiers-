from app import create_app

app = create_app()

if __name__ == "__main__":
    # accessible en local sur le réseau (utile pour tester depuis un téléphone
    # connecté au même wifi pendant le développement)
    app.run(host="0.0.0.0", port=5000, debug=True)
