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
sudo postgresql-setup --initdb --unit postgresql
#
echo "*****************************************"
echo "postgresql.conf update"
echo "*****************************************"
#
sudo cp -r -v postgresql.conf /var/lib/pgsql/data/postgresql.conf
#
echo "*****************************************"
echo "pg_hba.conf update"
echo "*****************************************"
#
sudo cp -r -v pg_hba.conf /var/lib/pgsql/data/pg_hba.conf
#
echo "*****************************************"
echo "database creation"
echo "*****************************************"
#
sudo service postgresql start
#
sudo -u postgres createdb helloworld
