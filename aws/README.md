# infrastructure-as-a-code

Our vision of infrastructure as a code defines an infrastructure definition based on a configuration file and a set of tasks to offer idempotent execution providing infrastructure states. Basically, we have created an orchestration procedure based on Red Hat Ansible official modules.

Unlike other tools, we have tried to define a simple and unique source of data to define multi-providers architectures based on dictionaries. This approach is an abstraction layer to facilitate architecture operators tasks. It is important to bear in mind that each file defines an architecture version and the execution of this procedure with a specific architecture file allows the user to generate an architecture state unequivocal.

As an added value within this orchestration procedure and as feature differential to other provision tools, we have the possibility of implement other tools integration in the orchestration pipeline and, for example, apply day 2 procedures as instances customization (DNS, hostname, Users, install packages, up/down services...) or PCI-DSS v3 Control Baseline implementation.


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

-   Programatic access account
-   Choose a specfic AWS Region
-   AWS VPC ID
-   Virtual Project ID
-   SSH Key which is refered in instances settings

Object creation supported:

-   Instances
-   Subnets
-   Security Groups

License
-------

BSD

Author Information
------------------

 Asier Cidon - Cloud Consultant

 asier.cidon@redhat.com
   