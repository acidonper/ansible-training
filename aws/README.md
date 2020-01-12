# infrastructure-as-a-code

The vision of infrastructure as a code defines an infrastructure definition based on a configuration file and a set of tasks to offer idempotent execution providing infrastructure states. Basically, It has been created an orchestration procedure based on Red Hat Ansible official modules.

Unlike other tools, this tool has tried to define a simple and unique source of data to define multi-providers architectures based on dictionaries.

This approach is an abstraction layer to facilitate architecture operators tasks. It is important to bear in mind that each file defines an architecture version based on **environment-version** and the execution of this procedure with a specific architecture file allows the user to generate an architecture state unequivocal.

As an added value within this orchestration procedure and as feature differential to other provision tools, it has the possibility of implement other tools integration in the orchestration pipeline and, for example, apply day 2 procedures as instances customization (DNS, hostname, Users, install packages, up/down services...) or PCI-DSS v3 Control Baseline implementation.


## AWS

There are a set of important aspects which have to be in mind:

-   Architecture state is generated at virtual project and vpc level. Virtual project is an object tag on each AWS resource.
-   Any object created is tagged with project and Name and these tags implement object unique identity.
-   Objects in a virtual project which are not defined in architecture file will be removed.
-   This automation process does not modify instances configuration. If it is necessary new instance settings, please add an instance with different name and parameters.

In order to be able to connect to AWS environment, it is necessary the following environment variables are defined:

-   AWS_ACCESS_KEY_ID (Example: AKIAUB6PFQFMROZERWWS)
-   AWS_SECRET_ACCESS_KEY (Example: ASDERASD+XL87CFBeoaqZXQD6J7v6X44TR0oEi)
-   AWS_REGION (Example: eu-west-1)

Requirements:

-   AWS Programatic access account
-   Choose a specfic AWS Region
-   AWS VPC ID
-   Generate a Virtual Project ID
-   SSH Key which is included in instances settings

Object creation supported:

-   Instances
-   Subnets
-   Security Groups

## Configurable Resources

In order to create the objects which have been included above, It is required to include their definition in a variables file and configure the inventory file in order to link the Ansible Tower installation.

### vars

-   aws-*environment*-*version*.yml -> Configuration as a code file which includes project_id, ec2_vpc_id, subnets and security_groups definitions.
-   vault-vars.yml -> Includes private variables which are used in order to context the environment.

### inventory

This inventory file is not required because these procedures generate dynamic inventories.

## Requirements

The below requirements are needed on the host that executes this module.

-   aws>=0.2.5
-   awscli>=1.16.153
-   decorator>=4.4.0
-   boto>=2.49.0
-   boto3>=1.9.171
-   botocore>=1.12.126

## Procedure

The programmatic procedure includes both the creation and deletion of the objects in AWS. On the other hand, It has been included some playbooks additionally in order to context the environment and generate an human-readable inventory.


### Playbooks

-   aws-iac.yml -> Using aws-*environment*-*version*.yml file, deploy all items defined in AWS
-   aws-iac-context-rhel-environment.yml -> Using both aws-*environment*-*version*.yml and  vault-vars.yml files, configure the instances deployed:
    -   Generate a dynamic environment base on AWS information
    -   Register RHEL machines in Red Hat CDN
    -   Create a new user and define the password for this user
    -   Change hostname
    -   Configure de SSH keys
    -   Install a set of packages
-   aws-iac-generate-inventory.yml ->  Using both aws-*environment*-*version*.yml and  vault-vars.yml files, generate an human-readable inventory in order to share information about the enviromment.
-   aws-iac-destroy.yml -> Using aws-*environment*-*version*.yml file, delete all items defined in AWS

### Examples

-   Create objects in AWS
```
$ ansible-playbook aws-iac.yml --extra-vars="ENV=preproduction VER=latest"
```

-   Configure AWS instances
```
$ ansible-playbook aws-iac-context-rhel-environment.yml --extra-vars="ENV=preproduction VER=latest" --ask-vault-pass
```

-   Generate AWS human-readable inventory
```
$ ansible-playbook aws-generate-inventory.yml --extra-vars="ENV=preproduction VER=latest"
```

-   Delete objects in AWS
```
$ ansible-playbook aws-iac-destroy.yml --extra-vars="ENV=preproduction VER=latest"
```

Note
---

This repository includes only AWS provider definition. Please, ask to the author for more information about other providers.

License
-------

BSD

Author Information
------------------

 Asier Cidon - Cloud Consultant

 asier.cidon@redhat.com
   