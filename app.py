from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    html = "<h1> This is a Flask App containerised with Docker</h1>"
    return html.format(format)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=port, debug=True)