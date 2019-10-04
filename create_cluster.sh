#!/usr/bin/env bash

eksctl create cluster -r us-west-2 -n timemachine-cluster -t t2.small
kubectl apply -f eks/deployment.yml
kubectl apply -f eks/services.yml
