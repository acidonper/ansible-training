# Job Templates

A job template is a definition and set of parameters for running an Ansible job. Job templates are useful to execute the same job many times. Job templates also encourage the reuse of Ansible playbook content and collaboration between teams. To execute a job, Tower requires that you first create a job template.

## Prerequisites

-   Go to https://github.com/join in a web browser. 
-   Go to your new repository
-   Click on "Create new file"
-   Introduce "ansible-playbook.yml"
-   The playbook should use tasks to ensure that the following conditions are met on the managed hosts:
    -   "Hosts" has to be defined to "all2
    -   Define a new variable named "testvar01" with a random content
    -   Debug "testvar01" variable content
-   Click on "Commit new file"

***NOTE: It is important to update Ansible Tower Project or to be selected "update on launch" option in Job Template configuration***

## Steps

-   Access Ansible Tower Interface
-   Select TEMPLATES
-   Click on + 
-   Select "Job Template"
-   Complete the "Job Template" form using the following entries:
    -   Name: ``<studentxx>``First Job Template
    -   Description: First Job Template
    -   Organization: ``<studentxx>``
    -   Project: ``<studentxx>``First Project
    -   Inventory: ``<studentxx>``First Inventory
    -   Credentials: ``<studentxx>``Machine Credential
    -   Playbook: ansible-playbook.yml
-   Click on ADD SURVEY
-   Create the following survey items:
    -   Prompt: Variable01
    -   Description: First testvar01
    -   Answer Variable Name: testvar01
    -   Answer Type: Text
    -   Check "Required"
-   Click on ADD
-   Click on SAVE
-   Click on + 
-   Select "Job Template"
-   Complete the "Job Template" form using the following entries:
    -   Name: ``<studentxx>``Second Job Template
    -   Description: Second Job Template
    -   Organization: ``<studentxx>``
    -   Project: ``<studentxx>``Second Project
    -   Inventory: ``<studentxx>``Second Inventory
    -   Credentials: ``<studentxx>``Machine Credential
    -   Playbook: ansible-playbook.yml
-   Click on ADD SURVEY
-   Create the following survey items:
    -   Prompt: Variable01
    -   Description: First testvar01
    -   Answer Variable Name: testvar01
    -   Answer Type: Text
    -   Check "Required"
-   Click on ADD
-   Click on SAVE
-   Execute the new Job Templates!!

License
-------

BSD

Author Information
------------------

 Asier Cidon - Cloud Consultant

 asier.cidon@redhat.com
