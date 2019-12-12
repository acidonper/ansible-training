# Projects 

Projects are logical collections of Ansible playbooks in Ansible Tower. These playbooks either reside on the Ansible Tower instance, or in a source code version control system supported by Tower.

## Prerequisites

### GITHUB

Your free GitHub account gives you unlimited access to public and private software repositories

-   Go to https://github.com/join in a web browser. 
-   Introduce username and password and "Sign in"
-   Go to your image (At top right) and "your repositories"
-   Click on New
-   Introduce Repository Name, Description and Select "Private" option. Please select "Initialize this repository with a README".
-   Click on "Create Repository"

## Steps

-   Access Ansible Tower Interface
-   Select PROJECTS
-   Click on +
-   Complete the credential form using the following entries:
    -   Name: ``<studentxx>`` First Project
    -   Description: First Project
    -   Organization: ``<studentxx>``
    -   SCM Type: Git
    -   SCM URL: (* Your new Github Repository URL)
    -   SCM Branch: master
    -   SCM Credentials: ``<studentxx>`` GitHub Credential
-   Click on SAVE
-   Click on PROJECTS
-   Click on "Get Latest SCM Version - Icon"


License
-------

BSD

Author Information
------------------

 Asier Cidon - Cloud Consultant

 asier.cidon@redhat.com