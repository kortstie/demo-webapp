import os
from flask import Flask, render_template
from kubernetes import client, config

app = Flask(__name__)

@app.route('/')
def home():
    config.load_incluster_config()
    
    version_api = client.VersionApi()
    k8s_version_info = version_api.get_code()
    k8s_version = k8s_version_info.git_version
    
    core_api = client.CoreV1Api()
    nodes = core_api.list_node().items

    node_data = []
    for node in nodes:
        node_name = node.metadata.name
        nodepool_name = node.metadata.labels.get('agentpool', 'Unknown')
        failure_domain_zone = node.metadata.labels.get('failure-domain.beta.kubernetes.io/zone', 'Unknown')
        failure_domain_region = node.metadata.labels.get('failure-domain.beta.kubernetes.io/region', 'Unknown')
        cpu_capacity = node.status.capacity.get('cpu', 'Unknown')
        memory_capacity = node.status.capacity.get('memory', 'Unknown')

        node_data.append({
            'node_name': node_name,
            'nodepool_name': nodepool_name,
            'failure_domain_zone': failure_domain_zone,
            'failure_domain_region': failure_domain_region,
            'cpu_capacity': cpu_capacity,
            'memory_capacity': memory_capacity
        })
    
    return render_template('index.html', k8s_version=k8s_version, node_data=node_data)