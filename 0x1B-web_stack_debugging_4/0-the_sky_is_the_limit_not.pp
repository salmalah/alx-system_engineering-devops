# File: 0-the_sky_is_the_limit_not.pp
# Description: Puppet manifest to optimize Nginx configuration
exec { 'ncrease-limit':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

exec { 'restart-nginx':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
