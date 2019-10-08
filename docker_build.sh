buildtag=$(git rev-parse --short HEAD)

# Step 1:
# Build image and add a descriptive tag
docker build . --tag y3key/timemachine-kube:$buildtag

# Step 2: 
# List docker images
#docker images -a
docker image ls