import os
from flask import Flask, render_template
from kubernetes import client, config

app = Flask(__name__)

@app.route('/')
def home():
    node_name = os.getenv('NODE_NAME', 'Unknown')
    
    config.load_incluster_config()
    
    version_api = client.VersionApi()
    k8s_version_info = version_api.get_code()
    k8s_version = k8s_version_info.git_version
    
    core_api = client.CoreV1Api()
    node_info = core_api.read_node(name=node_name)
    nodepool_name = node_info.metadata.labels.get('agentpool', 'Unknown')
    failure_domain_zone = node_info.metadata.labels.get('failure-domain.beta.kubernetes.io/zone', 'Unknown')
    failure_domain_region = node_info.metadata.labels.get('failure-domain.beta.kubernetes.io/region', 'Unknown')
    
    return render_template('index.html', k8s_version=k8s_version, node_name=node_name, nodepool_name=nodepool_name, failure_domain_zone=failure_domain_zone, failure_domain_region=failure_domain_region)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

