#!/usr/bin/env bash
# Sets up a web server for deploying a static website using Nginx

# Install Nginx if not already installed
sudo apt-get update
sudo apt-get install -y nginx

# Define website directory
WEB_DIR="/data/web_static"

# Create necessary directories and index.html file
sudo mkdir -p "$WEB_DIR/releases/test/" 
sudo mkdir -p "$WEB_DIR/shared/"
echo "Holberton School" > $WEB_DIR/releases/test/index.html

# Create symbolic link
sudo ln -sf "$WEB_DIR/releases/test/" "$WEB_DIR/current"

chown -R ubuntu /data/
chgrp -R ubuntu /data/

printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /var/www/html;
    index  index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }

    location /redirect_me {
        return 301 http://cuberule.com/;
    }

    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}" > /etc/nginx/sites-available/default

# Give ownership to ubuntu user and group
#sudo chown -R ubuntu:ubuntu "$WEB_DIR"

# Define Nginx configuration file
#NGINX_CONFIG="/etc/nginx/sites-available/web_static"

# Write Nginx configuration
#sudo tee "$NGINX_CONFIG" > /dev/null <<EOF
#server {
    #listen 80;
    #server_name theprincess.tech;

    #location /hbnb_static/ {
        #alias $WEB_DIR/current/;
        #index index.html index.htm;
   #}

    #access_log /var/log/nginx/theprincess.tech_access.log;
    #error_log /var/log/nginx/theprincess.tech_error.log;
#}
#EOF

# Enable the site by creating a symbolic link
#sudo ln -sf "$NGINX_CONFIG" "/etc/nginx/sites-enabled/"

# Restart Nginx
sudo service nginx restart

exit 0

