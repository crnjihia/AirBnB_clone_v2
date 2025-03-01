# Configures a web server for deployment of web_static.

# Nginx configuration string
$nginx_conf = "server {
    listen 80 default_server;  # Listen on port 80 for HTTP requests
    listen [::]:80 default_server;  # Listen on IPv6 as well
    add_header X-Served-By ${hostname};  # Add a custom header with the hostname
    root   /var/www/html;  # Set the document root
    index  index.html index.htm;  # Specify default index files

    # Configuration for serving static files
    location /hbnb_static {
        alias /data/web_static/current;  # Serve files from this alias
        index index.html index.htm;  # Specify default index files for this location
    }

    # Redirect requests to /redirect_me to a specified URL
    location /redirect_me {
        return 301 https://th3-gr00t.tk;  # Permanent redirect
    }

    error_page 404 /404.html;  # Custom error page for 404 errors

    # Internal location for handling 404 errors
    location /404 {
      root /var/www/html;  # Specify the root for internal 404 errors
      internal;  # Deny direct access to this location
    }
}"

# Ensure Nginx package is installed
package { 'nginx':
  ensure   => 'present',  # Ensure the package is present
  provider => 'apt'  # Use apt as the package provider
} ->

# Create /data directory
file { '/data':
  ensure  => 'directory'  # Ensure it is a directory
} ->

# Create /data/web_static directory
file { '/data/web_static':
  ensure => 'directory'  # Ensure it is a directory
} ->

# Create /data/web_static/releases directory
file { '/data/web_static/releases':
  ensure => 'directory'  # Ensure it is a directory
} ->

# Create /data/web_static/releases/test directory
file { '/data/web_static/releases/test':
  ensure => 'directory'  # Ensure it is a directory
} ->

# Create /data/web_static/shared directory
file { '/data/web_static/shared':
  ensure => 'directory'  # Ensure it is a directory
} ->

# Create an index.html file in the test release
file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',  # Ensure the file is present
  content => "Holberton School Puppet\n"  # Content of the index file
} ->

# Create a symbolic link to the current release
file { '/data/web_static/current':
  ensure => 'link',  # Ensure it is a symbolic link
  target => '/data/web_static/releases/test'  # Target of the link
} ->

# Change ownership of the /data directory recursively
exec { 'chown -R ubuntu:ubuntu /data/':
  path => '/usr/bin/:/usr/local/bin/:/bin/'  # Specify paths for the exec command
}

# Create /var/www directory
file { '/var/www':
  ensure => 'directory'  # Ensure it is a directory
} ->

# Create /var/www/html directory
file { '/var/www/html':
  ensure => 'directory'  # Ensure it is a directory
} ->

# Create an index.html file in the /var/www/html directory
file { '/var/www/html/index.html':
  ensure  => 'present',  # Ensure the file is present
  content => "Holberton School Nginx\n"  # Content of the index file
} ->

# Create a custom 404 error page
file { '/var/www/html/404.html':
  ensure  => 'present',  # Ensure the file is present
  content => "Ceci n'est pas une page\n"  # Content of the 404 page
} ->

# Configure Nginx with the specified configuration
file { '/etc/nginx/sites-available/default':
  ensure  => 'present',  # Ensure the file is present
  content => $nginx_conf  # Use the previously defined Nginx configuration
} ->

# Restart Nginx to apply the new configuration
exec { 'nginx restart':
  path => '/etc/init.d/'  # Specify paths for the exec command
}
