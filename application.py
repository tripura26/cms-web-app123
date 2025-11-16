from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def index():
    return "CMS is running successfully!"

if __name__ == '__main__':
    app.run(debug=True)
