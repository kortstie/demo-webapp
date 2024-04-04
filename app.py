import os
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    node_name = os.getenv('NODE_NAME', 'Unknown')
    return render_template('index.html', node_name=node_name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

