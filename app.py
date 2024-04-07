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
    
    apps_v1_api = client.AppsV1Api()
    deployment = apps_v1_api.read_namespaced_deployment(name='demo', namespace='demo')
    replicas = deployment.status.replicas

    pod_data = []
    pods = core_api.list_namespaced_pod(namespace='demo').items
    for pod in pods:
        if pod.metadata.labels.get('app') == 'demo':
            pod_name = pod.metadata.name
            pod_status = pod.status.phase
            pod_node = pod.spec.node_name

            pod_data.append({
                'pod_name': pod_name,
                'pod_status': pod_status,
                'pod_node': pod_node
            })

    node_data = []
    for node in nodes:
        node_name = node.metadata.name
        nodepool_name = node.metadata.labels.get('agentpool', 'Unknown')
        failure_domain_zone = node.metadata.labels.get('failure-domain.beta.kubernetes.io/zone', 'Unknown')
        failure_domain_region = node.metadata.labels.get('failure-domain.beta.kubernetes.io/region', 'Unknown')
        cpu_capacity = node.status.capacity.get('cpu', 'Unknown')
        memory_capacity_gb = round(int(node.status.capacity['memory'].strip('Ki')) / 1024 / 1024, 2)
        pod_count = sum(pod.spec.node_name == node_name for pod in pods)
        node_status = 'Unknown'
        for condition in node.status.conditions:
            if condition.type == 'Ready':
                node_status = condition.status
        is_cordoned = node.spec.unschedulable or False
        

        node_data.append({
            'node_name': node_name,
            'nodepool_name': nodepool_name,
            'failure_domain_zone': failure_domain_zone,
            'failure_domain_region': failure_domain_region,
            'cpu_capacity': cpu_capacity,
            'memory_capacity': memory_capacity_gb,
            'pod_count': pod_count,
            'node_status': node_status,
            'is_cordoned': is_cordoned
        })
    
    return render_template('index.html', k8s_version=k8s_version, node_data=node_data, replicas=replicas, pod_data=pod_data)
