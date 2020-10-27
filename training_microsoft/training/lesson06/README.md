# WorkFlow Template

The basic idea of a workflow is to link multiple Job Templates together. They may or may not share inventory, Playbooks or even permissions. The links can be conditional: 

* if job template A succeeds, job template B is automatically executed afterwards
* but in case of failure, job template C will be run. 

And the workflows are not even limited to Job Templates, but can also include project or inventory updates.

TIP: This enables new applications for Tower: different Job Templates can build upon each other. E.g. the networking team creates playbooks with their own content, in their own Git repository and even targeting their own inventory, while the operations team also has their own repos, playbooks and inventory.

In this lab you'll learn how to setup a workflow. 

## Prerequisites

-   ``<studentxx>`` Azure Inventory
-   Azure Credentials (_Provided by the instructor_)
-   ``<studentxx>`` First Project
-   ``<studentxx>`` Create Windows VM in Azure

## Steps

### Clone Provision Machine Job Template

-   Access Ansible Tower Interface
-   Select TEMPLATES
-   _"Copy Job Template"_ ``<studentxx>`` Create Windows VM in Azure
-   Click _``<studentxx>`` Create Windows VM in Azure@XX:XX:XX PM_
    -   Name: ``<studentxx>`` - WorkFlow00 - Create Windows VM in Azure
    -   Click on EDIT SURVEY
        - Click on DELETE SURVEY
-   Click on SAVE

### Create Install Security Updates Job Template

-   Access Ansible Tower Interface
-   Select TEMPLATES
-   Click on + 
-   Select "Job Template"
-   Complete the "Job Template" form using the following entries:
    -   Name: ``<studentxx>`` - WorkFlow02 - Install Security Updates in Windows VM
    -   Description: Install Security Updates in Windows VM
    -   Project: ``<studentxx>`` First Project
    -   Inventory: ``<studentxx>`` Azure
    -   Limit: ``<studentxx>``
    -   Credentials: ``<studentxx>`` Machine Credential
    -   Playbook: playbooks/windows-update-security-packages.yml
-   Click on SAVE

### Create Copy File Job Template

-   Access Ansible Tower Interface
-   Select TEMPLATES
-   Click on + 
-   Select "Job Template"
-   Complete the "Job Template" form using the following entries:
    -   Name: ``<studentxx>`` - WorkFlow03 - Copy File in Windows VM
    -   Description: Copy File in Windows VM
    -   Project: ``<studentxx>`` First Project
    -   Inventory: ``<studentxx>`` Azure
    -   Limit: ``<studentxx>``
    -   Credentials: ``<studentxx>`` Machine Credential
    -   Playbook: playbooks/windows-copy-files.yml
-   Click on SAVE

### Create Install package

-   Access Ansible Tower Interface
-   Select TEMPLATES
-   Click on + 
-   Select "Job Template"
-   Complete the "Job Template" form using the following entries:
    -   Name: ``<studentxx>`` - WorkFlow04 - Install Package in Windows VM
    -   Description: Install Package in Windows VM
    -   Project: ``<studentxx>`` First Project
    -   Inventory: ``<studentxx>`` Azure
    -   Limit: ``<studentxx>``
    -   Credentials: ``<studentxx>`` Machine Credential
    -   Playbook: playbooks/windows-install-package.yml
-   Click on SAVE


### Create Test package

-   Access Ansible Tower Interface
-   Select TEMPLATES
-   Click on + 
-   Select "Job Template"
-   Complete the "Job Template" form using the following entries:
    -   Name: ``<studentxx>`` - WorkFlow05 - Test Package installed in Windows VM
    -   Description:  Test Package installed in Windows VM
    -   Project: ``<studentxx>`` First Project
    -   Inventory: ``<studentxx>`` Azure
    -   Limit: ``<studentxx>``
    -   Credentials: ``<studentxx>`` Machine Credential
    -   Playbook: playbooks/windows-test-package.yml
-   Click on SAVE


### Create Complete Workflow Job Template

-   Access Ansible Tower Interface
-   Select TEMPLATES
-   Click on + 
-   Select "Workflow Template"
-   Complete the "Job Template" form using the following entries:
    -   Name: ``<studentxx>`` - WorkFlow - Deploy and Context Windows VM in Azure
    -   Description: Deploy and Context Windows VM in Azure
    -   Inventory: ``<studentxx>`` Azure
-   Click on SAVE

-   Config Workflow (*Its a procedure name, please follow next steps)
    -   Click on START
    -   Select ``<studentxx>`` - WorkFlow00 - Create Windows VM in Azure
    -   Click on SELECT
    -   Click on +
    -   Select Inventory Sync
    -   Select Azure
    -   Click on SELECT
    -   Click on +
    -   Select ``<studentxx>`` - WorkFlow02 - Install Security Updates in Windows VM
    -   Click on SELECT
    -   Click on +
    -   Select ``<studentxx>`` - WorkFlow03 - Copy File in Windows VM
    -   Click on SELECT
    -   Click on +
    -   Select ``<studentxx>`` - WorkFlow04 - Install Package in Windows VM
    -   Click on SELECT
    -   Click on +
    -   Select ``<studentxx>`` - WorkFlow05 - Test Package installed in Windows VM
    -   Click on SELECT
    -   Click on SAVE

-   Config Survey (*Its a procedure name, please follow next steps)
    -   Click on ADD SURVEY
    -   Create the following survey item:
        -   Prompt: Windows Version
        -   Description: Microsoft Windows Version
        -   Answer Variable Name: win_os_version
        -   Answer Type: Multi Choice (Single Select)
        -   Multi Choice Select:
            -  "2008-R2-SP1",
            -  "2012-Datacenter",
            -  "2012-R2-Datacenter",
            -  "2016-Nano-Server",
            -  "2016-Datacenter-with-Containers",
            -  "2016-Datacenter",
            -  "2019-Datacenter",
            -  "2019-Datacenter-Core",
            -  "2019-Datacenter-Core-smalldisk",
            -  "2019-Datacenter-Core-with-Containers",
            -  "2019-Datacenter-Core-with-Containers-smalldisk",
            -  "2019-Datacenter-smalldisk",
            -  "2019-Datacenter-with-Containers",
            -  "2019-Datacenter-with-Containers-smalldisk"
        -   Default Answer:  2016-Datacenter
        -   Check "Required"
    -   Click on ADD
    -   Create the following survey item:
        -   Prompt: Windows VM Size
        -   Description: Microsoft Windows VM Size
        -   Answer Variable Name: win_vm_size
        -   Answer Type: Multi Choice (Single Select)
        -   Multi Choice Select:
            -  Standard_D3_v3
            -  Standard_D2_v3
            -  Standard_B1ms
        -   Default Answer:  Standard_B1ms
        -   Check "Required"
    -   Click on ADD
    -   Create the following survey item:
        -   Prompt: Windows VM Username
        -   Description: Microsoft Windows Username
        -   Answer Variable Name: azure_win_username
        -   Answer Type: Text
        -   Check "Required"
    -   Click on ADD
    -   Create the following survey item:
        -   Prompt: Windows VM Password
        -   Description: Microsoft Windows Password
        -   Answer Variable Name: azure_win_password
        -   Answer Type: Password
        -   Minimum length: 12
        -   Maximum length: 32
        -   Check "Required"
    -   Click on ADD
    -   Click on SAVE

-   **Push the rocket to trigger the new Workflow Template!!** with the following settings:
    -   Windows Version -> 2016-Datacenter
    -   Windows VM Size -> Standard_B1ms
    -   Windows VM Username -> ``<studentxx>`` (*Defined in Credentials step*)
    -   Windows VM Username -> ``<studentxx>``  (*Defined in Credentials step*)


License
-------

BSD

Author Information
------------------

 Asier Cidon - Cloud Consultant

 asier.cidon@redhat.com
