#!/usr/bin/env bash
# Sets up a web server for deploying a static website using Nginx

# Install Nginx if not already installed
sudo apt-get update
sudo apt-get -y install nginx

# Define website directory
WEB_DIR="/data/web_static"

# Create necessary directories and index.html file
sudo mkdir -p "$WEB_DIR/releases/test/" "$WEB_DIR/shared/"
sudo tee "$WEB_DIR/releases/test/index.html" > /dev/null <<EOF
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
EOF

# Create symbolic link
sudo ln -sf "$WEB_DIR/releases/test/" "$WEB_DIR/current"

# Give ownership to ubuntu user and group
sudo chown -R ubuntu:ubuntu "$WEB_DIR"

# Define Nginx configuration file
NGINX_CONFIG="/etc/nginx/sites-available/web_static"

# Write Nginx configuration
sudo tee "$NGINX_CONFIG" > /dev/null <<EOF
server {
    listen 80;
    server_name theprincess.tech;

    location /hbnb_static/ {
        alias $WEB_DIR/current/;
        index index.html index.htm;
    }

    access_log /var/log/nginx/theprincess.tech_access.log;
    error_log /var/log/nginx/theprincess.tech_error.log;
}
EOF

# Enable the site by creating a symbolic link
sudo ln -sf "$NGINX_CONFIG" "/etc/nginx/sites-enabled/"

# Restart Nginx
sudo systemctl restart nginx

exit 0

