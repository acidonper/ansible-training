# Install Ansible Tower

Ansible Tower helps you manage your entire infrastructure. Easily pull your inventory from public cloud providers such as Amazon Web Services, Microsoft Azure, and more, or synchronize from your local OpenStack cloud or VMware environment.

In order to play with this amazing solution, this demo includes a set of steps to prepare a High Availability Ansible Tower Environment. 

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
ip-172-31-2-180.eu-west-1.compute.internal
ip-172-31-2-51.eu-west-1.compute.internal
ip-172-31-2-122.eu-west-1.compute.internal

[database]
ip-172-31-3-27.eu-west-1.compute.internal

[all:vars]
admin_password='xxxxxxx'

pg_host='ip-172-31-3-27.eu-west-1.compute.internal'
pg_port='5432'

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