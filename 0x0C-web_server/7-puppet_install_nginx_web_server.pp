# Install Nginx server using Puppet

exec {'install':
    provider => 'shell',
    command  => 'sudo apt-get update ; sudo apt-get -y install nginx ; echo "Hello world!" | sudo tee /var/www/html/index.html ; sudo sed -i "s/server_name_;/server_name_;\n\trewrite ^ \/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent; /etc/nginx/sites-available/default ; sudo service nginx start',
} 

