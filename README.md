# K8s flask demo app

## Purpose of this repo

- deploy an app to show some information about the k8s cluster and nodes
- presentation how an app distributes over different nodes and zones using a k8s topology spread
- show how an app gets deployed using github actions

## Prerequisites

- k8s cluster up and running, I will use an azure aks using the steps in my [repo here](https://github.
com/kortstie/azure-aks-setup-manual)
- fork this repo to your own github account

## HowTo deploy this app

### Setup github secrets

- github web ui: go to settings --> Secrets and variables --> Actions
- create the following secrets

| Secret Name | Secret Value |
|-------------|--------------|
| REGISTRY_LOGIN_SERVER     | your acr login server (kortstieacr.azurecr.io)       |
| RESOURCE_GROUP     | your resource group (kortstierg)       |
| AZURE_CREDENTIALS     | complete output of the **az ad sp ...** command       |
| REGISTRY_USERNAME | clientId value (xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx) |
| REGISTRY_PASSWORD | clientSecret value |

### 





