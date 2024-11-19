from src.web import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True) # HOT RELOAD. TODO: DISABLE FOR LAUNCH
