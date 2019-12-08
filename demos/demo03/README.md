# Ansible Tower Configuration as a Code

This demo implements Red Hat Ansible Tower configuration as a Code. 

## Resources

### vars

-   tower-config.yml -> Configuration as a code file which includes organization, users, teams, projects, credentials and Job Template definitions. On the other hand, includes connection parameters to Ansible Tower Cluster installed.

### inventory

This inventory file includes an IP and hostname which will be used to execute configuration tasks

### Playbooks

-   tower-configuration-deploy.yml -> Using tower-config.yml file, deploy all items in Ansible Tower
-   tower-configuration-undeploy.yml -> Using tower-config.yml file, delete all items in Ansible Tower

License
-------

BSD

Author Information
------------------

 Asier Cidon - Cloud Consultant

 asier.cidon@redhat.com


