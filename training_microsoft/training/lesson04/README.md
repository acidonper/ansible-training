# Inventories

An Inventory is a collection of hosts against which jobs may be launched, the same as an Ansible inventory file. Inventories are divided into groups and these groups contain the actual hosts. Groups may be populated manually, by entering host names into Tower, from one of Ansible Tower’s supported cloud providers or through dynamic inventory scripts.


## Prerequisites

-   Azure Credential (_Provided by the instructor_)

## Steps

-   Access Ansible Tower Interface
-   Select INVENTORIES
-   Click on + 
-   Select Inventory
-   Complete the credential form using the following entries:
    -   Name: ``<studentxx>`` Azure
    -   Description: Azure Inventory
    -   Organization: ``<studentxx>``
    -   Variables:
```
---
ansible_connection: "winrm"
ansible_winrm_server_cert_validation: ignore
ansible_ssh_port: 5986
```

-   Click on SAVE
-   Click on SOURCES
-   Click on + 
    -   Host Name: Azure
    -   Source: Microsoft Azure Resource Manager
    -   Credential: Azure
-   Click on SAVE
-   Click on _Sync All_

License
-------

BSD

Author Information
------------------

 Asier Cidon - Cloud Consultant

 asier.cidon@redhat.com