# RestApi-Flask-PostgreSQL
A RestApi using Flask and PostgreSQL in AWS EC2 instance

EC2 setting up,
- Services > Compute > EC2 > Launch intance
- Amazon Linux 2 AMI > t2.micro > Next: Configure instance 
- Advanced details | as text 

#!/bin/bash 
sudo yum update -y
sudo yum install python-pip git -y
pip install --user virtualenv

- skip to Configure Security Group > Type: All traffic
- Review and Launch > Launch
- Create a new key pair > name = ec2 (will be downloaded your local) >Launch instances

ssh to EC2 instance (MobaXterm),
- Basic SSH Settings | Remote host = 34.238.249.178 (public ip of ec2 instance) > Specify username = ec2-user > port:22
- Advanced SSH settings | Use private key > select ec2.pem > OK



