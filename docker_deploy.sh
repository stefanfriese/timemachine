buildtag=$(git rev-parse --short HEAD)

echo "Deployment Step: docker push..."
docker push y3key/timemachine-kube:$buildtag

echo "Deployment Step: kubectl set image..."
kubectl set image -n default deployment/timemachine-deployment timemachine=y3key/timemachine-kube:$buildtag

echo "Deployment finished."
