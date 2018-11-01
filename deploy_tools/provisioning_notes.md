Configure New Website
====================

##The Required Packages

* nginx
* python3
* git
* pip
* virtualenv

Ubuntu Operation
sudo apt-get install nginx git python3-pip
sudo pip3 install virtualenv

##Configure Nginx Virtual Machine
* refer to nginx-template
* replace SITE with the target URL, like www.tonycodetest.site

##Systemd Service
* refer to gunicorn-template
* replace SITE with the target URL, like www.tonycodetest.site

##Archive Structure
/home/username
--sites
  --SITE
    --database
    --source
    --static
    --virtualenv

