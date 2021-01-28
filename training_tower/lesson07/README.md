# Ansible Tower Role Based Access Control

## Steps Summary

- Create the following users:
    -   ``<studentxx>``-developer01
    -   ``<studentxx>``-developer02
    -   ``<studentxx>``-developer03
    -   ``<studentxx>``-developer04
- Create the following teams:
    -   ``<studentxx>``-teamdevelopers
    -   ``<studentxx>``-teamoperators

## Steps

-   Access Ansible Tower Interface
-   Select USERS
-   Click on + 
-   Complete "new user" form using the following entries:
    -   First Name: ``<studentxx>``-developer01
    -   Last Name: ``<studentxx>``-developer01
    -   Organization: ``<studentxx>``
    -   Email: ``<studentxx>``-developer01@developer01.com
    -   UserName: ``<studentxx>``-developer01
    -   Password: ``<studentxx>``-developer01
    -   Confirm Password: **********
-   Click on SAVE
-   Click on + 
-   Complete "new user" form using the following entries:
    -   First Name: ``<studentxx>``-developer02
    -   Last Name: ``<studentxx>``-developer02
    -   Organization: ``<studentxx>``
    -   Email: ``<studentxx>``-developer02@developer02.com
    -   UserName: ``<studentxx>``-developer02
    -   Password: ``<studentxx>``-developer02
    -   Confirm Password: **********
-   Click on SAVE
-   Click on + 
-   Complete "new user" form using the following entries:
    -   First Name: ``<studentxx>``-operator01
    -   Last Name: ``<studentxx>``-operator01
    -   Organization: ``<studentxx>``
    -   Email: ``<studentxx>``-operator01@operator01.com
    -   UserName: ``<studentxx>``-operator01
    -   Password: ``<studentxx>``-operator01
    -   Confirm Password: **********
-   Click on SAVE
-   Click on + 
-   Complete "new user" form using the following entries:
    -   First Name: ``<studentxx>``-operator02
    -   Last Name: ``<studentxx>``-operator02
    -   Organization: ``<studentxx>``
    -   Email: ``<studentxx>``-operator02@operator02.com
    -   UserName: ``<studentxx>``-operator02
    -   Password: ``<studentxx>``-operator02
    -   Confirm Password: **********
-   Click on SAVE

-   Select TEAMS
-   Click on + 
-   Complete "new team" form using the following entries:
    -   Name: ``<studentxx>``-teamdevelopers
    -   Description: ``<studentxx>``-teamdevelopers
    -   Organization: ``<studentxx>``
-   Click on SAVE
-   Click on + 
-   Complete "new team" form using the following entries:
    -   Name: ``<studentxx>``-teamoperators
    -   Description: ``<studentxx>``-teamoperators
    -   Organization: ``<studentxx>``
-   Click on SAVE

## BONUS

- Assign users to teams:
    -   ``<studentxx>``-developer01 -> ``<studentxx>``-teamdevelopers
    -   ``<studentxx>``-developer02 -> ``<studentxx>``-teamdevelopers
    -   ``<studentxx>``-developer03 -> ``<studentxx>``-teamoperators
    -   ``<studentxx>``-developer04 -> ``<studentxx>``-teamoperators

- Assign roles to teams:
    -   Job Templates -> Added ``<studentxx>``-teamdevelopers as admin
    -   Job Templates -> Added ``<studentxx>``-teamoperators as execute

- Access and test permissions

License
-------

BSD

Author Information
------------------

 Asier Cidon - Cloud Consultant

 asier.cidon@redhat.com
