# Azure SQL Database 

## Prerequisites

-   Azure Credentials (_Provided by the instructor_)
-   ``<studentxx>`` First Project

## Steps

-   Access Ansible Tower Interface
-   Select TEMPLATES
-   Click on + 
-   Select "Job Template"
-   Complete the "Job Template" form using the following entries:
    -   Name: ``<studentxx>`` Create SQL Database
    -   Description: Create SQL Database
    -   Project: ``<studentxx>`` First Project
    -   Inventory: ``<studentxx>`` Azure
    -   Credentials: Azure
    -   Playbook: playbooks/windows-azure-create-db.yml
-   Click on ADD SURVEY
-   Create the following survey item:
    -   Prompt: SQL Database Name
    -   Description: SQL Database Name
    -   Answer Variable Name: sql_database
    -   Answer Type: Text
    -   Check "Required"
-   Click on ADD
-   Click on SAVE

-   **Push the rocket to trigger the new Job Template!!**
    -   SQL Database Name -> ``<database_name>``


License
-------

BSD

Author Information
------------------

 Asier Cidon - Cloud Consultant

 asier.cidon@redhat.com
