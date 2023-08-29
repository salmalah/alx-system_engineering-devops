# Install Nginx web server
class nginx_config {
    package { 'nginx':
        ensure => 'installed',
    }

    file { '/var/www/html/index.html':
        content => 'Hello World!',
    }

    file { '/etc/nginx/sites-available/default':
        ensure => 'file',
        source => 'puppet:///modules/nginx_config/default',
        require => Package['nginx'],
    }

    file { '/etc/nginx/sites-enabled/default':
        ensure => 'link',
        target => '/etc/nginx/sites-available/default',
        require => File['/etc/nginx/sites-available/default'],
    }

    service { 'nginx':
        ensure => 'running',
        enable => true,
        require => File['/etc/nginx/sites-enabled/default'],
    }
}

class { 'nginx_config': }

nginx::resource::vhost { 'default':
    www_root     => '/var/www/html',
    index_files  => ['index.html'],
    listen_port  => 80,
    redirect     => true,
    redirect_status => 'permanent',
    redirect_from => '^/redirect_me$',
    redirect_to   => 'https://www.youtube.com/watch?v=QH2-TGUlwu4',
}
