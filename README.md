# AnsibleApi

The purpose of this API is to receive a JSON string (Ansible Playbooks) as a POST Request from a client to execute Ansible Tasks.
Look at [AnsibleWeb](https://github.com/skrijeljhasib/AnsibleWeb) for a frontend Application.

## Motivation

As a trainee at Flash Europe International, I was engaged during 3 months to create this project with AnsibleWeb.
The [AnsibleWeb](https://github.com/skrijeljhasib/AnsibleWeb) needs the AnsibleApi to install a virtual machine with packages and a little configuration in openstack clouds.

## Getting started

### Prerequisites

```
sudo add-apt-repository ppa:ansible/ansible
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install apache2
sudo apt-get install python-bottle
sudo apt-get install python-shade
sudo a2enmod cgi
sudo a2enmod rewrite
sudo apt install ansible
```

### Installation

Download and extract the project. Place it in your Apache DocumentRoot folder.


You have to create a ssh key and add it with nova to your openstack cloud (In the project folder):
```
cd config
mkdir keys
cd keys
sudo -u www-data ssh-keygen -t rsa
sudo nova --os-username username --os-password password --os-project-name projectname --os-auth-url authurl --os-region-name regionname --os-project-id projectid keypair-add --pub-key yourpublickey
```

Change Permissions (In the project folder):
```
cd config
sudo chgrp www-data hosts
sudo chgrp www-data keys
```

Add this to your Apache Configuration file:

```
WSGIScriptAlias / /var/www/html/AnsibleApi/app.wsgi
<Directory /var/www/html/AnsibleApi >
        Options +ExecCGI
        DirectoryIndex index.py
</Directory>
AddHandler cgi-script .py
```

### Configuration (Optional)

If you want to change the path to the config/ansible.cfg file,
you have to copy the file to the new directory and change the settings in the app.ini file.


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

