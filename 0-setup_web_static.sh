#!/usr/bin/env bash
#sets up your web servers for the deployment of web_static

# Install Nginx if not already installed
sudo apt-get update
sudo apt-get -y install nginx

# Create necessary directories
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo touch /data/web_static/releases/test/index.html
echo "<html><head></head><body>Test HTML file</body></html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
config_block="
server {
    listen 80;
    server_name theprincess.tech;

    location /hbnb_static/ {
        alias /data/web_static/current/;
        index index.html index.htm;
    }

    access_log /var/log/nginx/theprincess.tech_access.log;
    error_log /var/log/nginx/theprincess.tech_access.log;
}
"
sudo sed -i "/# Only/ i $config_block" /etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx restart

exit 0
