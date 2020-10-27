# Job Templates

A job template is a definition and set of parameters for running an Ansible job. Job templates are useful to execute the same job many times. Job templates also encourage the reuse of Ansible playbook content and collaboration between teams. To execute a job, Tower requires that you first create a job template.

## Prerequisites

-   ``<studentxx>`` Azure Inventory
-   Azure Credentials (_Provided by the instructor_)
-   ``<studentxx>`` First Project

## Steps

-   Access Ansible Tower Interface
-   Select TEMPLATES
-   Click on + 
-   Select "Job Template"
-   Complete the "Job Template" form using the following entries:
    -   Name: ``<studentxx>`` Create Windows VM in Azure
    -   Description: Create Windows VM in Azure
    -   Project: ``<studentxx>`` First Project
    -   Inventory: ``<studentxx>`` Azure
    -   Credentials: Azure
    -   Playbook: playbooks/windows-azure-instance-deployment.yml
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
-   **Push the rocket to trigger the new Job Template!!** with the following settings:
    -   Windows Version -> 2016-Datacenter
    -   Windows VM Size -> Standard_B1ms
    -   Windows VM Username -> ``<studentxx>`` (*Defined in Credentials step*)
    -   Windows VM Username -> ``<studentxx>``  (*Defined in Credentials step*)


Lastly, try to connect to this new machine by RDP using the IP which you can find in the logs:

```
"msg": "The public IP is 51.132.21.102. Used to connect with RDP"
```

```
# Example in Fedora or rhel8
/usr/bin/xfreerdp /v:<publicIP> /u:<azure_win_username> /p:<azure_win_password> /cert:ignore
```

License
-------

BSD

Author Information
------------------

 Asier Cidon - Cloud Consultant

 asier.cidon@redhat.com
