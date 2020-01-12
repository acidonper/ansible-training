# Ansible Tower Configuration as a Code

Red Hat Ansible Tower configuration as a Code includes a procedure to configure an Ansible Tower installation creating and configuring some objects through a programmatic procedure. 

The following list includes the Ansible Tower's elements which can be created and configured in this procedure:

-   Organization
-   Users
-   Teams
-   Projects
-   Credentials
-   Job Templates


## Configurable Resources

In order to create the objects which have been included above, It is required to include their definition in a variables file and configure the inventory file in order to link the Ansible Tower installation.

### vars

-   tower-config.yml -> Configuration as a code file which includes organization, users, teams, projects, credentials and Job Template definitions. On the other hand, includes connection parameters to Ansible Tower Cluster installed.

### inventory

This inventory file includes an IP and hostname which will be used to execute configuration tasks


## Requirements

The below requirements are needed on the host that executes this module.

-   ansible-tower-cli >= 3.0.2

## Procedure

The programmatic procedure includes both the creation and deletion of the objects.

### Playbooks

-   tower-configuration-deploy.yml -> Using tower-config.yml file, deploy all items in Ansible Tower
-   tower-configuration-undeploy.yml -> Using tower-config.yml file, delete all items in Ansible Tower

### Examples

-   Deploy Red Hat Ansible Tower programmatic configuration
```
$ ansible-playbook -i inventory tower-configuration-deploy.yml -k -K
```

-   Delete Red Hat Ansible Tower programmatic configuration
```
$ ansible-playbook -i inventory tower-configuration-undeploy.yml -k -K
```

License
-------

BSD

Author Information
------------------

 Asier Cidon - Cloud Consultant

 asier.cidon@redhat.com


