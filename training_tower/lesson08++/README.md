# Emulate a real Ansible Tower Project

This lesson tries to emulate a real Ansible Tower Project where it is necessary to implement some Job Templates (Playbooks) and execute them in a chained way.

From an overall point of view, this new project has to implement the folowing tasks:
-   Create a set of users
-   Configure NTP server
-   Install mariadb
-   Up and Enable mariadb service
-   Install httpd
-   Configure httpd in order to create two new virtualHosts in ports (80 and 81)
-   Up and Enable mariadb service
-   Create dynamically web pages in Apache folders

## Prerequisites

In order to implement this lesson, it is necessary to have some previous lessons' objects defined. The following list includes these objects required and lessons where they were created:

-   ``<studentxx>`` GitHub Credential (lesson02)
-   ``<studentxx>`` First Project (lesson03)
-   ``<studentxx>`` First Inventory (lesson04)

On the other hand, it is necessary to develop a set of new playbooks in order to implement the tasks previously described:

-   Go to https://github.com/join in a web browser. 
-   Go to your new repository
-   Click on "Create new file"
-   Introduce "manageusers-playbook.yml"
-   The playbook should use tasks to ensure that the following conditions are met on the managed hosts (*using become)):
    -   "Hosts" has to be defined to "all"
    -   Create a new users which are defined in a variable named "users" (user01 by default)
    -   Create a new file in users' home named "user_created_date.txt" with creation new user time.
-   Click on "Commit new file"
-   Click on "Create new file"
-   Introduce "configurentp-playbook.yml"
-   The playbook should use tasks to ensure that the following conditions are met on the managed hosts (*using become):
    -   "Hosts" has to be defined to "all"
    -   Install required packages in order to make available rhel-system-roles
    -   Configure NTP server using a variable named "ntp_server" (time.google.com by default)
-   Click on "Commit new file"
-   Click on "Create new file"
-   Introduce "mariadb-playbook.yml"
-   The playbook should use tasks to ensure that the following conditions are met on the managed hosts (*using become):
    -   "Hosts" has to be defined to "all"
    -   Install required packages in order to make available mariadb server and client
    -   Up and Enable mariadb service
-   Click on "Commit new file"
-   Click on "Create new file"
-   Introduce "mariadb-services-playbook.yml"
-   The playbook should use tasks to ensure that the following conditions are met on the managed hosts (*using become):
    -   "Hosts" has to be defined to "all"
    -   Implement a new taskswhich has to be able to manage mariadb service state from a variable named "mysql_service_state" (restarted by default)
-   Click on "Commit new file"
-   Click on "Create new file"
-   Introduce "httpd-playbook.yml"
-   The playbook should use tasks to ensure that the following conditions are met on the managed hosts (*using become):
    -   "Hosts" has to be defined to "all"
    -   Install required packages in order to make available http server and php 
    -   Create a new file named "index.html" in httpd' default folder
    -   Create a new file named "info.php" in httpd' default folder which displays php info page
    -   Up and Enable httpd service
-   Click on "Commit new file"
-   Click on "Create new file"
-   Introduce "httpd-services-playbook.yml"
-   The playbook should use tasks to ensure that the following conditions are met on the managed hosts (*using become):
    -   "Hosts" has to be defined to "all"
    -   Implement a new task which has to be able to manage httpd service state from a variable named "httpd_service_state" (restarted by default)
-   Click on "Commit new file"
-   Click on "Create new file"
-   Introduce "fail-playbook.yml"
-   The playbook should use tasks to ensure that the following conditions are met on the managed hosts (*using become):
    -   "Hosts" has to be defined to "all"
    -   Implement a fail task in order to throw an error when this playbook will be executed
-   Click on "Commit new file"

**BONUS ACTIVITY**

-   Click on "Create new file"
-   Introduce "httpd-virtualhosts-playbook.yml"
-   The playbook should use tasks to ensure that the following conditions are met on the managed hosts (*using become):
    -   "Hosts" has to be defined to "all"
    -   Implement a new task which has to be able to create a set of virtualhost provided by a new variable named "virtualhost_ports" (80 and 81 by default)
-   Click on "Commit new file" 
-   Click on "Create new file"
-   Introduce "httpd-content-playbook.yml"
-   The playbook should use tasks to ensure that the following conditions are met on the managed hosts (*using become):
    -   "Hosts" has to be defined to "all"
    -   Implement a new task which has to be able to obtain the number of ports httpd is listening
    -   Create a new file named "index.html" in each virtualhost's default folder including the virtualhost's port number (Find and example in ./examples/index.html)
    -   Create a new file named "info.php" in each virtualhost's default folder which displays php info page
    -   Create a new file named "information.php" in each virtualhost's default folder including the following information:
-   Click on "Commit new file" 

## Important

It is important to bear in mind:

-   Use become whenever required
-   All variables have to be introduced by a Survey but it is necessary to define default values in the SURVEY and in the playbook as well
-   Update Ansible Tower Project or to be selected "update on launch" option in Job Template configuration
-   Pay special attention to "Create a new file..." tasks because it is possible to need new files in the repository
-   ***BONUS ACTIVITY** These playbooks will need Jinja2 templates

## Steps

### Create Job Templates

Firstly, it is necessary to create a new "Job Template" for each new playbook in the repository. Please, follow the instructions listed bellow:

-   Access Ansible Tower Interface
-   Select TEMPLATES
-   Click on + 
-   Select "Job Template"
-   Complete the "Job Template" form using the following entries:
    -   Name: [LESSON08] ``<studentxx>`` Job Template ``<playbook_name>.yml``
    -   Description: Job Template ``<playbook_name>``
    -   Project: ``<studentxx>``First Project
    -   Inventory: ``<studentxx>``First Inventory
    -   Credentials: ``<studentxx>``Machine Credential
    -   Playbook: ``<playbook_name>.yml``
-   Click on ADD SURVEY

***When it is required***

-   Create the following survey items:
    -   Prompt: ``<variable_name>``
    -   Description: ``<variable_name>``
    -   Answer Variable Name: ``<variable_name>``
    -   Answer Type: Text or Multiple Choise (multiple select)
    -   Default Answer: ``<variable_default_values>``
    -   Check "Required"
-   Click on ADD
-   Click on SAVE

**Always**

- Test the Job Template!!

### Create Workflow Templates

Now is the time to integrate all Job Templates. For this reason, it is necessary to create a new Workflow Template and add all Job Templated created in order to:

-   Create five new users (``<studentxx>``-user01...``<studentxx>``-user05)
-   Install/configure ntp server (us.pool.ntp.org)
-   Install mysql server
-   Restart mysql server
-   Install httpd server
-   ***BONUS*** Configure a couple of new VirtualHosts which listen 80 and 81 ports located in /var/www/html/service1-80 and /var/www/html/service2-81 and create their respective web pages
-   Restart httpd server

To achieve this objective, it will also necessary to include all Job Templates created in a new workflow. The following list includes some instructions about the implementation process:

-   Access Ansible Tower Interface
-   Select TEMPLATES
-   Click on + 
-   Select "Workflow Template"
-   Complete the "Workflow Template" form using the following entries:
    -   Name: [LESSON08] ``<studentxx>`` Workflow Job Template 
    -   Description: ``<studentxx>`` Workflow Job Template 
    -   Organization: ``<studentxx>``
-   Click on SAVE
-   Click on START
-   Select [LESSON08] ``<studentxx>`` Job Template manageusers-playbook.yml
-   Click on PROMPT
-   Introduce a new value 
-   Click on NEXT 
-   Click on CONFIRM
-   Click on SELECT
-   Click on +
-   Select [LESSON08] ``<studentxx>`` Job Template fail-playbook.yml
-   Click on SELECT
-   Click on +
-   Select [LESSON08] ``<studentxx>`` Job Template configurentp-playbook.yml.yml
-   Click on PROMPT 
-   Introduce a new value 
-   Click on NEXT
-   Click on CONFIRM
-   **Select in RUN field ->  On Failure**
-   Click on SELECT
***Please repeate the following proceess wih the remaining Job Templates***
-   Select [LESSON08] ``<studentxx>`` Job Template ``<playbook_name>.yml``
-   Click on PROMPT (* If it is required)
-   Introduce a new value (* If it is required)
-   Click on NEXT (* If it is required)
-   Click on CONFIRM (* If it is required)
-   Click on SELECT
...
-   Click on SAVE
-   Execute the new Workflow Template!!


License
-------

BSD

Author Information
------------------

 Asier Cidon - Cloud Consultant

 asier.cidon@redhat.com
