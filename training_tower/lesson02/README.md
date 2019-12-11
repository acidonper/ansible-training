# Credentials

Credentials are utilized by Tower for authentication when launching Jobs against machines, synchronizing with inventory sources, and importing project content from a version control system. Credential configuration can be found in the Settings.

Tower credentials are imported and stored encrypted in Tower, and are not retrievable in plain text on the command line by any user. You can grant users and teams the ability to use these credentials, without actually exposing the credential to the user.

There are many types of credentials including machine, network, and various cloud providers. In this workshop, we are using a machine credential.

## Prerequisites

### GITHUB

Your free GitHub account gives you unlimited access to public and private software repositories

-   Go to https://github.com/join in a web browser. 
-   Enter your personal details. In addition to creating a username and entering an email address, you'll also have to create a password. Your password must be at least 15 characters in length or at least 8 characters with at least one number and lowercase letter.
-   Click Select a Plan
-   Click Choose Free
-   Welcome to GitHub

## Steps

- Access Ansible Tower Interface
- Select CREDENTIALS
- Click on +
- Complete the credential form using the following entries:
    -   Name: ``<studentxx>`` GitHub Credential
    -   Description: Credentials GitHub
    -   Organization: Default
    -   Type: Source Control
    -   Username: GitHub username
    -   Password: GitHub password
- Click on SAVE
- Click on +
- Complete the credential form using the following entries:
    -   Name: ``<studentxx>`` Machine Credential
    -   Description: Machine Credential
    -   Organization: Default
    -   Type: Machine
    -   Username: studentxx
    -   Password: ``<student_pass>``
- Click on SAVE

License
-------

BSD

Author Information
------------------

 Asier Cidon - Cloud Consultant

 asier.cidon@redhat.com