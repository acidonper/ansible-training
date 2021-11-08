# Red Hat Ansible Automation Platform 2.0

## Introduction

TBD
 
## Setting Up a Execution Environment

- Create the execution environment container

```$bash
cd ansible20
ansible-builder build -f execution-environment.yml -t quay.io/acidonpe/ansible20:1.1
```

- Push the new execution environment to a container registry

```$bash
podman images
podman push quay.io/acidonpe/ansible20:1.1
```

## Author 

Asier Cidon

asier.cidon@redhat.com
