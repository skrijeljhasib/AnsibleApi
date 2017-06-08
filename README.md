# AnsibleApi

The purpose of this API is to play Ansible Playbooks. It receives a JSON string as a POST Request to execute Ansible Tasks.
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
sudo a2enmod wsgi
sudo a2enmod headers
```

### Installation

Download the project and place it in your Apache2 DocumentRoot folder.

#### Apache Requirement :

Apache Configuration file example:
```
DocumentRoot /var/www/html/AnsibleApi-x.y.z/
WSGIScriptAlias / /var/www/html/AnsibleApi-x.y.z/app.wsgi
```

Change Permissions (In the project folder):
```
sudo chgrp www-data config/local
sudo chmod g+w config/local
cd config/local
sudo chgrp www-data hosts
sudo chmod g+w hosts
sudo mkdir keys
sudo chown -R www-data keys
```

#### Nova Requirement :
You have to create a ssh key and add it with nova to your openstack cloud (In the project folder):
```
cd config/local/keys
sudo -u www-data ssh-keygen -t rsa
Enter file in which to save the key: (path-example: /var/www/html/AnsibleApi-x.y.z/config/local/keys/id_rsa)

sudo touch known_hosts
sudo chown www-data known_hosts
sudo chgrp www-data known_hosts

nova --os-username username --os-password password --os-project-name projectname --os-auth-url authurl --os-region-name regionname --os-project-id projectid keypair-add --pub-key id_rsa nameofkey
```

### Configuration

Look at the config/local/app.ini file.

Look at config/local/ansible.cfg file.

* ssh_args = -o UserKnownHostsFile=/var/www/html/AnsibleApi-x.y.z/config/local/keys/known_hosts
* private_key_file = /var/www/html/AnsibleApi-x.y.z/config/local/keys/id_rsa

### Finally 

* sudo service apache2 restart

## Test

Use [Postman](https://www.getpostman.com/):

* URL: **IP-Address or Domain-Name to AnsibleApi with portnumber**/post_data
* METHOD: POST
* BODY RAW JSON: 
```
    {
       "name": "Test Shell",
       "hosts": "localhost",
       "gather_facts": "false",
       "tasks": [
                   {
                     "shell": "ls -l"
                   }
       ]
    }

```

## Contributors

* Skrijelj Hasib

## License
The GNU General Public License v3.0 - GPL-3.0
