# A Puppet manifest to create a custom HTTP header response

exec {'update':
  command => '/usr/bin/apt-get update',
}

package {'nginx':
  ensure  => 'present', 
}
file_line {'http_header',
  path    => '/etc/nginx/nginx/conf',
  line    => 'add_header X-Served-By $hostname;',
  match   => 'http {',
  notify  => Exec['nginx_reload'],
}

exec { 'nginx_reload':
  command => '/usr/sbin/service nginx reload',
}
