*****
iRODS
*****

.. bibliographic fields (which also require a transform):
:author: Juan Medina
:contact: medinaj@mskcc.org
:organization: Memorial Sloan-Kettering
:status: This is "work in progress"
:date: |date|

:abstract:
    This wiki describes the **leukid** and it's models. The **leukid** is constructed based on the information provided by the **sample_form**.

    Typographical conventions:

    * ``constant width`` for code fragments, commands or object attributes
    * *italic* for file names
    * **bold** important terms

.. meta::
   :keywords: irods
   :description lang=en: This wiki describes how to install *iRODS*.

.. contents:: Table of Contents
.. .. section-numbering::


Requirements
============

• What's the hardware?

• Support search and preservation of the sequencing data; What metadata needs to be collected?

• Determine who can access the site and whether they are employees, photographers, or subscribers.

• To ensure the site can grow over time, determine if and when data should be archived or deleted, and when expanding the storage configuration will be necessary. Can we afford downtime?

• Disk failures occur, so we will want to keep at least two copies of the data, located on separate disks, at all times?

Data:
• Where is Leukgen’ data located - one central location or distributed?

• What are the advantages and shortcomings of having the data in a central location; how about distributed? What do you think is the best course of action?

• Will Leukgen need multiple copies of data objects or is a single copy sufficient? What do you think is best?

• How much data does Leukgen currently have? Is this a stable quantity or could it increase over time? How quickly could Leukgen generate new data?

• What file formats will the data come in? Are these proprietary or open?

• Is any of the data proprietary or confidential?

Network
• What speed is the Leukgen network? How consistently is that speed maintained?

• What security is in place?

Resources
• Does Leukgen have a budget for ongoing software costs? For software engineers?

• What is Leukgen’ stance on open source? How does this factor into their decision-making process?

• What resources does Leukgen have in place to manage a data repository (e.g., technical staff, support options, site licenses, hardware)?

Organization
• What is Leukgen’ organizational structure?

• Will you, the Data Center Administrator, have autonomous decision-making or will you need to get executive buy-in?

• Who is accountable for and affected by any decisions?

Users
• What kinds of users will need access to the data? What types of access or privileges will they need?

• How many users does Leukgen anticipate? Is this a stable quantity or could it increase over time?

• Where are the users located? What time zone? Are they located near the data or somewhere else?

Also consider the needs of specific classes of users:
• Leukgen scientists.
• Administrators.


Installation
============

dzdo nano /etc/hosts
    127.0.0.1   plvleukweb1 localhost etc...
    ::1         localhost etc...

ping -c 3 plvleukweb1
    64 bytes from plvleukweb1 (127.0.0.1): icmp_seq=1 ttl=64 time=0.014 ms
    64 bytes from plvleukweb1 (127.0.0.1): icmp_seq=2 ttl=64 time=0.022 ms
    64 bytes from plvleukweb1 (127.0.0.1): icmp_seq=3 ttl=64 time=0.023 ms

psql
    CREATE DATABASE "ICAT";
    CREATE USER irods WITH PASSWORD 'testpassword';
    GRANT ALL PRIVILEGES ON DATABASE "ICAT" to irods;

the core server software
    wget ftp://ftp.renci.org/pub/irods/releases/4.1.6/centos6/irods-icat-4.1.6-centos6-x86_64.rpm

the database plugin specific (PostgreSQL in our case)
    wget ftp://ftp.renci.org/pub/irods/releases/4.1.6/centos6/irods-database-plugin-postgres93-1.6-centos6-x86_64.rpm

Workflow automation section
    wget ftp://ftp.renci.org/pub/irods/training/training-example-1.0.deb


RPM install guide:
1.  Yum Install Required Dependencies ::

   -- Note - names may change slightly between different OS versions, which can be determined by 'yum search package-name'

      postgresql
      postgresql-server
      unixODBC
      perl
      authd

      AND

      postgresql-odbc  (could also be postgresqlXX-odbc)
       - also needs to be installed, but this is not declared in the RPM due to issues with versioning resolution

2.  Start Postgres Server and Initialize Database Tables ::

      CentOS 5.x :: sudo /sbin/service postgresql start
      CentOS 6.x :: sudo /sbin/service postgresql initdb; sudo /sbin/service postgresql start
      SUSE11     :: sudo /usr/sbin/rcpostgresql start
      OpenSUSE12 :: sudo /usr/sbin/rcpostgresql start

3.  Modify authd config file for xinetd.d ::

      vim /etc/xinetd.d/auth

    Remove the '-E' command line argument for auth ::

      changing :
        [ server_args = -t60 --xerror --os -E ]
      to :
        [ server_args = -t60 --xerror --os ]

4.  Set the proper runlevel for authd ::

      sudo /sbin/chkconfig --level=3 auth on

5.  Restart xinetd

      sudo /etc/init.d/xinetd restart

[FAILED] 6.  Open your firewall, if necessary, to let in iRODS ::

      Add the following to your /etc/sysconfig/iptables:

        -A INPUT -m state --state NEW -m tcp -p tcp --dport 1247 -j ACCEPT
        -A INPUT -m state --state NEW -m tcp -p tcp --dport 1248 -j ACCEPT
        -A INPUT -m state --state NEW -m tcp -p tcp --dport 20000:20199 -j ACCEPT
        -A INPUT -m state --state NEW -m udp -p udp --dport 20000:20199 -j ACCEPT

      Restart the firewall:

        sudo service iptables restart

7.  Install the iRODS RPM ::

      rpm -i irods-XXX.rpm

SEE --->  Needed to do:
        dzdo yum install fuse-libs
        dzdo yum install perl-JSON

        dzdo su
            pip install psutil
            pip install requests
            pip install jsonschema

        wget http://dl.fedoraproject.org/pub/epel/6/i386/python-jsonschema-2.3.0-1.el6.noarch.rpm

        irods:
        dzdo rpm -i python-jsonschema-2.3.0-1.el6.noarch.rpm

        database plugin, 9.3 didnt work:
        wget ftp://ftp.renci.org/pub/irods/releases/4.1.6/centos6/irods-database-plugin-postgres-1.6-centos6-x86_64.rpm
        dzdo rpm -i irods-database-plugin-postgres-1.6-centos6-x86_64.rpm


Setup irods:
dzdo /var/lib/irods/packaging/setup_irods.sh


-------------------------------------------
iRODS service account name  irods
iRODS service group name    irods
iRODS Zone:                 tempZone
iRODS Port:                 1247
Range (Begin):              20000
Range (End):                20199
Vault Directory:            /var/lib/irods/iRODS/Vault
zone_key:                   TEMPORARY_zone_key
negotiation_key:            TEMPORARY_32byte_negotiation_key
Control Plane Port:         1248
Control Plane Key:          TEMPORARY__32byte_ctrl_plane_key
Schema Validation Base URI: https://schemas.irods.org/configuration
Administrator Username:     rods
Administrator Password:     leukrods
-------------------------------------------


-------------------------------------------
Database Type:     postgres
Hostname or IP:    localhost
Database Port:     5432
Database Name:     ICAT
Database User:     irods
Database Password: testpassword
-------------------------------------------


After this I needed to run:
    init
        One or more fields in your iRODS environment file (irods_environment.json) are
        missing; please enter them.
        Enter the host name (DNS) of the server to connect to: plvleukweb1
        Enter the port number: 1247
        Enter your irods user name: rods
        Enter your irods zone: tempZone
        Those values will be added to your environment file (for use by
        other iCommands) if the login succeeds.
        Enter your current iRODS password:


Create elli user as admin
    iadmin mkuser elli roduser
    iadmin moduser alice password elli


Create new resource
    iadmin mkresc newResc unixfilesystem \
        plvleukweb1:/var/lib/irods/iRODS/new_vault


The iadmin command can also be used to remove a user (using rmuser as the argument) or remove a resource (using rmresc as the argument). Use iadmin -h to learn more. Now that we're done with administrative commands, let's log out of iRODS.

Loggin with elli
    iexit full
    rm ~/.irods/irods_environment.json
    iinit

Give write permissions from owner
    ichmod -r write bobby training_jpgs

Create and trim replica in newResc
    irepl -R newResc training_jpgs/peanuts.jpg
    itrim -N 1 -S demoResc training_jpgs/peanuts.jpg

Create more resources and add them as childs to a replication resource
    iadmin mkresc storageResc1 unixfilesystem\
        learnervb.example.org:/var/lib/irods/storageVault1
    iadmin mkresc storageResc2 unixfilesystem\
        learnervb.example.org:/var/lib/irods/storageVault2
    iadmin mkresc replResc replication

    iadmin addchildtoresc replResc newResc
    iadmin addchildtoresc replResc storageResc1
    iadmin addchildtoresc replResc storageResc2

    ilsresc
        demoResc
        replResc:replication
        ├── newResc
        ├── storageResc1
        └── storageResc2

Decommissioning Storage
As our needs change, we may wish to decommission storage resources to use for other purposes. The following commands will remove storageResc1 from the resource tree so it can be repurposed.
    iadmin rmchildfromresc replResc storageResc1
    itrim -M -r -S storageResc1 /tempZone
    iadmin rmresc storageResc1
