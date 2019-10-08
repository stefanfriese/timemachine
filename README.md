# Udacity DevOps Capstone Project

This application can normalize dates:
* Normalize dates with different formats.
* Converts dates to unix timestamp.
* Converts unix timestamp to date.

The application provides an API. You can also use the swagger documentation.

## Setup

## Prerequisites
* AWS account available
* aws cli installed and configured to use access keys
* Kubernetes cli kubectl installed (at least v1.10)
* Amazon EKS cli eksctl installed (see: https://eksctl.io/introduction/installation/)

Execute ./create_cluster.sh
This script uses eksctl (for more information, see: https://eksctl.io/usage/creating-and-managing-clusters/)

### CI/CD Pipeline
If you change the code, the application gets deployed on Kubernetes after passing the CI/CD tests:
* Lint check
* Build docker image
* Deploy docker image to dockerhub
* Rolling update on EKS kubernetes cluster

## Local Run
You can also execute the application locally:
* Standalone:  `python3 app.py`
* Run in Docker:  `./docker_local.sh`
