# AnsibleApi

The purpose of this API is to to play Ansible Playbooks. It receives a JSON string as a POST Request to execute Ansible Tasks.
Look at [AnsibleWeb](https://github.com/skrijeljhasib/AnsibleWeb) for a frontend Application.

## Motivation

As a trainee at Flash Europe International, I was engaged during 3 months to create this project with AnsibleWeb.
The [AnsibleWeb](https://github.com/skrijeljhasib/AnsibleWeb) needs the AnsibleApi to install a virtual machine with packages and to configure the new machine in the openstack cloud.

## Getting started

AnsibleApi has been tested with ubuntu 16.04, apache2, python3.2 and ansible2.3.
It may work with alternative versions but is not currently documented.
Only Nova Openstack provider is created so far. New providers will be added in the feature. 

### Prerequisites

```
sudo add-apt-repository ppa:ansible/ansible
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install ansible
sudo apt-get install apache2
sudo apt-get install libapache2-mod-wsgi
sudo apt-get install python-bottle
sudo apt-get install python-shade
sudo apt-get install mysql-server
sudo a2enmod wsgi
sudo a2enmod rewrite
```

### Installation

Download and extract the project. Place it in your Apache2 DocumentRoot folder.

Nova Requirement :
You have to create a ssh key and add it with nova to your openstack cloud (In the project folder):
```
cd config
mkdir keys
cd keys
sudo -u www-data ssh-keygen -t rsa
sudo nova --os-username username --os-password password --os-project-name projectname --os-auth-url authurl --os-region-name regionname --os-project-id projectid keypair-add --pub-key yourpublickey
```

Apache Requirement :
Change Permissions (In the project folder):
```
cd config
sudo chgrp www-data hosts
sudo chgrp www-data keys
```

Apache Configuration file example :

```
WSGIScriptAlias / /var/www/html/AnsibleApi/app.wsgi
<Directory /var/www/html/AnsibleApi >
        Options +ExecCGI
        DirectoryIndex index.py
</Directory>
AddHandler cgi-script .py
```

### Configuration

Look at the config/app.ini file.

## Test

Use [Postman](https://www.getpostman.com/):

* URL: **IP-Address or Domain-Name to AnsibleApi**/post_data
* METHOD: POST
* BODY RAW JSON: 
```
[
    {
       "name": "Install Package(s)",
       "hosts": "localhost",
       "become": "true",
       "become_method": "sudo",
       "become_user": "root",
       "gather_facts": "false",
       "pre_tasks": [
                      {
                        "name": "Install Python",
                        "raw": "apt -y install aptitude python-apt"
                      }
       ],
       "tasks": [
                   {
                     "name": "Install Packages",
                     "apt": "name={{ item }} state=present",
                     "with_items": [
                                     "postfix",
                                     "munin-node"
                     ]
                   }
       ]
    }
]
```

## Contributors


## License

