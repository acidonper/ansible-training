# Inventories

An Inventory is a collection of hosts against which jobs may be launched, the same as an Ansible inventory file. Inventories are divided into groups and these groups contain the actual hosts. Groups may be populated manually, by entering host names into Tower, from one of Ansible Tower’s supported cloud providers or through dynamic inventory scripts.

## Steps

-   Access Ansible Tower Interface
-   Select INVENTORIES
-   Click on + 
-   Select Inventory
-   Complete the credential form using the following entries:
    -   Name: ``<studentxx>`` First Inventory
    -   Description: First Inventory
    -   Organization: ``<studentxx>``
-   Click on SAVE
-   Click on HOSTS
-   Click on + 
    -   Host Name: ``<ip-xx.eu-west-1.compute.internal>``
    -   Description: ``<studentxx>`` Internal AWS HostName
-   Click on SAVE


License
-------

BSD

Author Information
------------------

 Asier Cidon - Cloud Consultant

 asier.cidon@redhat.com