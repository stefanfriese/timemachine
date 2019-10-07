#!/usr/bin/env bash

eksctl create cluster -r us-east-1 -n timemachine-cluster -t t3.medium
kubectl apply -f eks/deployment.yml
kubectl apply -f eks/services.yml
