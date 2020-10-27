# Credentials

Credentials are utilized by Tower for authentication when launching Jobs against machines, synchronizing with inventory sources, and importing project content from a version control system. Credential configuration can be found in the Settings.

Tower credentials are imported and stored encrypted in Tower, and are not retrievable in plain text on the command line by any user. You can grant users and teams the ability to use these credentials, without actually exposing the credential to the user.

There are many types of credentials including machine, network, and various cloud providers. In this workshop, we are using a machine credential.

## Prerequisites

-   GitHub Repository

## Steps

### GitHub Credentials

- Access Ansible Tower Interface
- Select CREDENTIALS
- Click on +
- Complete the credential form using the following entries:
    -   Name: ``<studentxx>`` GitHub Credential
    -   Description: Credentials GitHub
    -   Organization: ``<studentxx>``
    -   Type: Source Control
    -   Username: ``<GitHub username>``
    -   Password: ``<GitHub password>``
- Click on SAVE

### Windows Machine Credentials

- Click on +
- Complete the credential form using the following entries:
    -   Name: ``<studentxx>`` Machine Credential
    -   Description: Machine Credential
    -   Organization: ``<studentxx>``
    -   Type: Machine
    -   Username: ``<studentxx>``
    -   Password: ``<studentxx_pass>`` (*Please the password must be minimum 12 digits, an uppercase digit, a lowercase digit and number)
    -   Privileged Escalation Method: runas
    -   Privileged Escalation Password: ``<studentxx_pass>``
- Click on SAVE

License
-------

BSD

Author Information
------------------

 Asier Cidon - Cloud Consultant

 asier.cidon@redhat.com