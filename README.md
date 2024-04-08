# K8s flask demo app

## Purpose of this repo

- deploy an app to show some information about the k8s cluster and nodes
- demonstrate how an app distributes over different nodes and zones using a k8s topology spread
- show how an app gets deployed using github actions

## Prerequisites

- k8s cluster up and running, I will use an azure aks using the steps in my [repo here](https://github.com/kortstie/azure-aks-setup-manual)
- fork this repo to your own github account

## HowTo deploy this app

### Setup github secrets

- github web ui: go to settings --> Secrets and variables --> Actions
- create the following secrets

| Secret Name | Secret Value |
|-------------|--------------|
| AZURE_CREDENTIALS     | complete output of the **az ad sp ...** command       |
| REGISTRY_USERNAME | clientId value (xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx) |
| REGISTRY_PASSWORD | clientSecret value |

- create the following repository variable

| Variable Name | Variable Value |
|-------------|--------------|
| PROJECT_NAME | your project name (kortstie) |


### What happens here?

- Each push in the main branch triggers the workflow stored in *.github/workflows*
- a github runner machine spins up (Ubuntu latest)
- checks out this repo into the runner machine
- builds a container image containing our flask app
- pushes the image to our acr container registry
- connects to our aks cluster
- deploys the k8s manifests

### Test it

    oc -n demo get service

Browse to the external IP, Port 5000 of the service!

### Things to do

- registry in "20-deployment.yaml" needs to be replaced automatically via sed








