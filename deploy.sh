buildtag=$(git rev-parse --short HEAD)

echo "Deployment Step 1/3: docker build..."
docker build . --tag y3key/timemachine-kube:$buildtag

echo "Deployment Step 2/3: docker push..."
docker push y3key/timemachine-kube:$buildtag

echo "Deployment Step 3/3: kubectl set image..."
kubectl set image deployment/timemachine-deployment timemachine=y3key/timemachine-kube:$buildtag

echo "Deployment finished."
