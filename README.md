Red Hat Ansible Training
---------------------------

Introduction 
--------------

Red Hat Ansible Training tries to give a general overview about Red Hat Ansible Engine and Red Hat Ansible Tower solutions, covering the most important concepts and elements inside these automation tools.

To support this objective, a set of practical laboratories have been included in this training in order to explore each point deeply and assist the student learning process to internalizing best practices and key concepts.

Folder Structure 
-----------------

A folder structure is provided in this repository in order to split laboratory content and improve the clarity of the training. The following folders have been included with a specific objective:

-   aws -> Includes environment a set up automatism in order to deploy and destroy laboratory environments.
-   example -> Includes son Ansible playbooks and roles which could be useful in a future steps.
-   training -> Lessons structure which includes specific exercises with solutions.

Laboratory Environment
------------------------

Amazon Web Services (AWS) is a subsidiary of Amazon that provides on-demand cloud computing platforms and APIs to individuals, companies, and governments, on a metered pay-as-you-go basis.

As you might know, Red Hat Ansible community supports several AWS modules which allow final customers to define and deploy multiples computing resources in this provider. In that way, this training makes use of these modules to deploy and destroy the environment dynamically based on number of users and resources the training needs.

This laboratory creates a complete environment which is ready to install an Ansible Tower and supports the implementation of proposed lessons in this training. The following list includes a summary about this environment:

-   30 instances for students
-   1 instance designed to support some Ansible Core's lessons
-   4 instances for install an Ansible Tower cluster 

In order to deploy this environment and make it available to execute training's lessons, it is necessary to follow the next steps: 

-   Deploy Red Hat Ansible Training Environment
```
$ ansible-playbook aws-iac.yaml
```

-   Configure Red Hat Ansible Training Environment
```
$ ansible-playbook aws-context-rhel-environment.yaml --ask-vault-pass
```

-   Obtain Red Hat Ansible Training Environment inventory
```
$ ansible-playbook aws-generate-inventory.yaml
```

Once the training is completed:

-   Destroy Red Hat Ansible Training Environment
```
$ ansible-playbook aws-iac-destroy.yaml 
```

Demos 
---------

Demos folder includes a set of ansible implementation examples. The following list includes a summary:

-   **Demo1** - Install Ansible Tower
-   **Demo2** - Navigate Ansible Tower Interface
-   **Demo3** - Ansible Tower Configuration as a Code

Lessons 
---------

Training folder includes The following list includes a lessons summary:

-   **Lesson 1** - Install Ansible
-   **Lesson 2** - Configure Ansible
-   **Lesson 3** - Ansible AdHoc Commands
-   **Lesson 4** - Ansible Inventory
-   **Lesson 5** - Ansible Playbooks
-   **Lesson 6** - Ansible Variable
-   **Lesson 7** - Ansible Facts
-   **Lesson 8** - Ansible Vault
-   **Lesson 9** - Ansible Conditionals, loops and delegation
-   **Lesson 10** - Ansible Handlers
-   **Lesson 11** - Ansible Templates
-   **Lesson 12** - Ansible Roles
-   **Lesson 13** - Ansible Filters
-   **Lesson 14** - Ansible Modules
-   **Lesson 15** - Ansible Lookups, Callbacks & Tags

License
-------

BSD

Author Information
------------------

 Asier Cidon - Cloud Consultant

 asier.cidon@redhat.com
   
