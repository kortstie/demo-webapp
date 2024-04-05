import os
from flask import Flask, render_template
from kubernetes import client, config

app = Flask(__name__)

@app.route('/')
def home():
    node_name = os.getenv('NODE_NAME', 'Unknown')
    config.load_incluster_config()
    v1 = client.VersionApi()
    k8s_version = v1.get_code()
    return render_template('index.html', node_name=node_name, k8s_version=k8s_version)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

