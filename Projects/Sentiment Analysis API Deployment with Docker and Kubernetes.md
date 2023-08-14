
Github : [sentiment-analysis](https://github.com/FelitaD/sentiment-analysis)
Local : [README](file:///Users/donor/PycharmProjects/sentiment-analysis/README.md) 

https://colab.research.google.com/drive/1CjO_OtzOt2bNEia_WD8cX8o6IoMYZO47#scrollTo=dgwVRnl0nu3L
  
## Sentiment Analysis API
  
After authentification, the user can provide a sentence that will yield a polarity score.
There are 2 versions of the sentence analyzer.
  
You can find the API documentation [here](https://documenter.getpostman.com/view/17951830/UVktpYz8)
  
## Tests
  
Basic tests using requests.
  
## Deployments
  
### Single-cluster deployment with Docker compose
  
2 containers :
- API
- Tests
  
### Multi-cluster deployment with Kubernetes
https://kubernetes.io/docs/tasks/configure-pod-container/translate-compose-kubernetes/  
  
```kompose convert```
  
Modifier dans api-deployment.yaml ```replicas: 3```
  
``` kubectl apply -f api-deployment.yaml,api-service.yaml,api-network-networkpolicy.yaml,app-volume-persistentvolumeclaim.yaml,test-analyzer-1-deployment.yaml,test-analyzer-2-deployment.yaml, test-login-deployment.yaml,test-permissions-deployment.yaml,test-status-deployment.yaml**``` 
  
```minikube service api```
