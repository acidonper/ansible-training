# Ansible Tower

Ansible Tower is a web-based UI that provides an enterprise solution for IT automation based on Ansible. Regarding features, Ansible Tower offers to the users the following main capabilities:

* Enterprise framework for controlling, securing and managing Ansible automation
* UI and restful API
* Role-based access control
* Push-button deployment
* Central logging - complete auditability and compliance
* And much more...

Ansible Tower is a Django web application designed to run on a Linux server as an on-premise, self-hosted solution which layers on top of an enterprise's existing Ansible infrastructure.

Tower stores its data in a PostgreSQL back-end database and makes use of the RabbitMQ messaging system. 

Components:
* HTTP service: webUI
* RabbitMQ: broker
* Celery: workers
* Memcached: cache

Depending on the needs of the enterprise, Ansible Tower can be implemented using one of the following architectures.

* Single Machine with Integrated Database. All Ansible Tower components, the web front-end, RESTful API back end, and PostgreSQL database, reside on a single machine. This is the standard architecture.
* Single Machine with Remote Database. The Ansible Tower web UI and RESTful API back end are installed on a single machine, and the PostgreSQL database is installed on another server on the same network. 
* High Availability Multi Machine Cluster. This architecture is now an active-active, high-availability cluster consisting of multiple active Ansible Tower nodes.
* OpenShift Pod with Remote Database. In this architecture, Red Hat Ansible Tower operates as a container-based cluster running on Red Hat OpenShift. The cluster runs on an OpenShift pod, which contains four containers to run the Ansible Tower components. OpenShift adds or removes pods to scale Ansible Tower up and down. 


## Steps

- Download Red Hat Ansible Tower Bundle Installation

```
$ wget https://releases.ansible.com/ansible-tower/setup-bundle/ansible-tower-setup-bundle-latest.el8.tar.gz
```

- Obtain Ansible Tower Bundle Content

```
$ tar -zxvf ansible-tower-setup-bundle-latest.el8.tar.gz
```

- Configure  Ansible Tower Architecture

```
$ cd ansible-tower-setup-bundle-3.6.1-1.el8/

$ vi inventory

[tower]
localhost ansible_connection=local

[database]

[all:vars]
admin_password='xxxxxxx'

pg_host=''
pg_port=''

pg_database='awx'
pg_username='awx'
pg_password='xxxxxxxx'
pg_sslmode='prefer'  # set to 'verify-full' for client-side enforced SSL

rabbitmq_username=tower
rabbitmq_password='xxxxxxxx'
rabbitmq_cookie=cookiemonster

ignore_preflight_errors=true

# Isolated Tower nodes automatically generate an RSA key for authentication;
# To disable this behavior, set this value to false
# isolated_key_generation=true

# SSL-related variables

# If set, this will install a custom CA certificate to the system trust store.
# custom_ca_cert=/path/to/ca.crt

# Certificate and key to install in nginx for the web UI and API
# web_server_ssl_cert=/path/to/tower.cert
# web_server_ssl_key=/path/to/tower.key

# Use SSL for RabbitMQ inter-node communication.  Because RabbitMQ never
# communicates outside the cluster, a private CA and certificates will be
# created, and do not need to be supplied.
# rabbitmq_use_ssl=False

# Server-side SSL settings for PostgreSQL (when we are installing it).
# postgres_use_ssl=False
# postgres_ssl_cert=/path/to/pgsql.crt
# postgres_ssl_key=/path/to/pgsql.key
```

- Run Setup Script

```
$ ./setup.sh
```

License
-------

BSD

Author Information
------------------

 Asier Cidon - Cloud Consultant

 asier.cidon@redhat.com