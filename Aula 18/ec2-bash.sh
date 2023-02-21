#!/bin/bash
sudo yum update -y
sudo yum install -y httpd.x86_64
systemctl start httpd.service
systemctl enable httpd.service
sudo echo “Hello Pet Store” > /var/www/html/index.html
