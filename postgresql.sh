#!/bin/bash 
#
echo "*****************************************"
echo "PostgreSQL installation"
echo "*****************************************"
#
sudo amazon-linux-extras install postgresql10=latest -y
#
sudo yum install postgresql postgresql-server postgresql-devel postgresql-contrib postgresql-docs -y
#
sudo service postgresql initdb 
#
sudo service postgresql start
#
sudo -u postgres psql 
CREATE DATABASE helloworld;
\q
sudo -u postgres psql createuser ec2-user
#
echo "*****************************************"
echo "postgresql.conf update"
echo "*****************************************"
#
sudo cp -r -v postgresql.conf /var/lib/pgsql/data/postgresql.conf
sudo service postgresql restart
#
echo "*****************************************"
echo "pg_hba.conf update"
echo "*****************************************"
#
sudo cp -r -v pg_hba.conf /var/lib/pgsql/data/pg_hba.conf
sudo service postgresql restart



