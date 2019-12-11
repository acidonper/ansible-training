# Ansible Tower Role Based Access Control

## Steps Summary

- Create the following users:
    -   developer01
    -   developer02
    -   developer03
    -   developer04
- Create the following teams:
    -   teamdevelopers
    -   teamoperators

## Steps

-   Access Ansible Tower Interface
-   Select USERS
-   Click on + 
-   Complete "new user" form using the following entries:
    -   First Name: developer01
    -   Last Name: developer01
    -   Organization: ``<studentxx>``
    -   Email: developer01@developer01.com
    -   UserName: developer01
    -   Password: developer01
    -   Confirm Password: **********
-   Click on SAVE
-   Click on + 
-   Complete "new user" form using the following entries:
    -   First Name: developer02
    -   Last Name: developer02
    -   Organization: ``<studentxx>``
    -   Email: developer02@developer02.com
    -   UserName: developer02
    -   Password: developer02
    -   Confirm Password: **********
-   Click on SAVE
-   Click on + 
-   Complete "new user" form using the following entries:
    -   First Name: operator01
    -   Last Name: operator01
    -   Organization: ``<studentxx>``
    -   Email: operator01@operator01.com
    -   UserName: operator01
    -   Password: operator01
    -   Confirm Password: **********
-   Click on SAVE
-   Click on + 
-   Complete "new user" form using the following entries:
    -   First Name: operator02
    -   Last Name: operator02
    -   Organization: ``<studentxx>``
    -   Email: operator02@operator02.com
    -   UserName: operator02
    -   Password: operator02
    -   Confirm Password: **********
-   Click on SAVE

-   Select TEAMS
-   Click on + 
-   Complete "new team" form using the following entries:
    -   Name: teamdevelopers
    -   Description: teamdevelopers
    -   Organization: ``<studentxx>``
-   Click on SAVE
-   Click on + 
-   Complete "new team" form using the following entries:
    -   Name: teamoperators
    -   Description: teamoperators
    -   Organization: ``<studentxx>``
-   Click on SAVE

## BONUS

- Assign users to teams:
    -   developer01 -> teamdevelopers
    -   developer02 -> teamdevelopers
    -   developer03 -> teamoperators
    -   developer04 -> teamoperators

- Assign roles to teams:
    -   Job Templates -> Added teamdevelopers as admin
    -   Job Templates -> Added teamoperators as execute

- Access and test permissions

License
-------

BSD

Author Information
------------------

 Asier Cidon - Cloud Consultant

 asier.cidon@redhat.com
