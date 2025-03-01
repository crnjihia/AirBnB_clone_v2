#!/usr/bin/env bash
# Script to set up web servers for the deployment of web_static

# Update the package list to get the latest version of packages
sudo apt-get update

# Install Nginx web server
sudo apt-get -y install nginx

# Allow HTTP traffic through the firewall for Nginx
sudo ufw allow 'Nginx HTTP'

# Create the main data directory
sudo mkdir -p /data/

# Create subdirectories for web_static storage
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

# Create a test HTML file in the test release directory
sudo touch /data/web_static/releases/test/index.html

# Write a simple HTML page into the test file
echo "<html>
  <head>
  </head>
  <body>
    ALX
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link to the test release as the current release
sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

# Change ownership of the /data/ directory to the ubuntu user
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to serve content from the web_static directory
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

# Restart Nginx to apply the new configuration
sudo service nginx restart
