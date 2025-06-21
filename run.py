from app import create_app  # <-- use app. since run.py is in root

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
