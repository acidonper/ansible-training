# WorkFlow Template

The basic idea of a workflow is to link multiple Job Templates together. They may or may not share inventory, Playbooks or even permissions. The links can be conditional: 

* if job template A succeeds, job template B is automatically executed afterwards
* but in case of failure, job template C will be run. 

And the workflows are not even limited to Job Templates, but can also include project or inventory updates.

TIP: This enables new applications for Tower: different Job Templates can build upon each other. E.g. the networking team creates playbooks with their own content, in their own Git repository and even targeting their own inventory, while the operations team also has their own repos, playbooks and inventory.

In this lab you'll learn how to setup a workflow. 

## Prerequisites

-   ``<studentxx>``First Job Template
-   ``<studentxx>``Second Job Template

## Steps

-   Access Ansible Tower Interface
-   Select TEMPLATES
-   Click on + 
-   Select "Workflow Template"
-   Complete the "Workflow Template" form using the following entries:
    -   Name: ``<studentxx>``First Job Template
    -   Description: First Job Template
    -   Organization: ``<studentxx>``
-   Click on SAVE
-   Click on START
-   Select ``<studentxx>`` First Job Template
-   Click on PROMPT
-   Introduce a new value
-   Click on NEXT
-   Click on CONFIRM
-   Click on SELECT
-   Click on +
-   Select ``<studentxx>`` Second Job Template
-   Select RUN -> Success
-   Click on PROMPT
-   Introduce a new value
-   Click on NEXT
-   Click on CONFIRM
-   Select SELECT
-   Click on SAVE
-   Execute the new Workflow Template!!


License
-------

BSD

Author Information
------------------

 Asier Cidon - Cloud Consultant

 asier.cidon@redhat.com
