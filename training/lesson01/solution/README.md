# Install Ansible

## Installing Control Node

Latest Release via DNF or Yum

* On RHEL7:

```
$ sudo subscription-manager repos --enable rhel-7-server-ansible-2.9-rpms
$ sudo yum install ansible
```

* On RHEL8:

```
$ sudo subscription-manager repos --enable ansible-2.9-for-rhel-8-x86_64-rpms
$ sudo dnf install ansible
```
