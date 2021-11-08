# Red Hat Ansible Automation Platform 2.0

## Introduction

Red Hat, Inc., the world's leading provider of open source solutions, announced Red Hat Ansible Automation Platform 2 as the company’s new standard for hybrid cloud automation. Refined for the evolving realities of computing at hybrid cloud scale, the latest version of the platform adds self-contained automation capabilities while shifting automation more deeply into the application development lifecycle.
 
## Setting Up an Execution Environment

- Create the execution environment definition (requirements reference, base image, etc)

```$bash
cd ansible20
vi requirements.yml
vi execution-environment.yml
```

- Build the execution environment container 

```$bash
ansible-builder build -f execution-environment.yml -t quay.io/acidonpe/ansible20:1.1
```

- Push the new execution environment to a container registry

```$bash
podman images
podman push quay.io/acidonpe/ansible20:1.1
```

## Red Hat Ansible Automation Platform Configuration Steps

- Create and sync the Ansible project
- Create a new execution environment based on the previous image pushed in the container registry
- Create a job template using the respective project and execution environment
## Author 

Asier Cidon

asier.cidon@redhat.com
