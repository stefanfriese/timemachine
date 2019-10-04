buildtag=$(git rev-parse --short HEAD)
docker build . --tag y3key/timemachine-kube:$buildtag
docker push y3key/timemachine-kube:$buildtag
kubectl set image deployment/timemachine-deployment y3key/timemachine-kube:$buildtag
