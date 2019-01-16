# RestApi-Flask-PostgreSQL
A RestApi using Flask and PostgreSQL in AWS EC2 instance

EC2 setting up,
- Services > Compute > EC2 > Launch intance
- Amazon Linux 2 AMI > t2.micro > Next: Configure instance 
- Advanced details | as text 

#!/bin/bash 
sudo yum update -y
sudo yum install python-pip git -y
sudo /usr/bin/easy_install virtualenv

- skip to Configure Security Group > Type: All traffic
- Review and Launch > Launch
- Create a new key pair > name = ec2 (will be downloaded your local) >Launch instances

ssh to EC2 instance (MobaXterm),
- Basic SSH Settings | Remote host = 34.238.249.178 (public ip of ec2 instance) > Specify username = ec2-user > port:22
- Advanced SSH settings | Use private key > select ec2.pem > OK

After login,
- $ git clone https://github.com/GurayCetin/RestApi-Flask-PostgreSQL
- $ cd RestApi-Flask-PostgreSQL

Install postgresql,
- $ sudo amazon-linux-extras install postgresql10=latest -y
- $ sudo yum install postgresql postgresql-server postgresql-devel postgresql-contrib postgresql-docs -y
- $ sudo service postgresql initdb 
- $ sudo service postgresql start
- $ sudo -u postgres psql 
\ CREATE DATABASE helloworld;
\q
- $ sudo -u postgres createuser ec2-user
- $ sudo cp -r -v postgresql.conf /var/lib/pgsql/data/postgresql.conf
- $ sudo service postgresql restart
- $ sudo cp -r -v pg_hba.conf /var/lib/pgsql/data/pg_hba.conf
- $ sudo service postgresql restart

virtual environment,
- $ virtualenv venv
- $ source venv/bin/activate
- $(venv) pip install -r requirements.txt

to run api,
- $(venv) pyhton api.py


