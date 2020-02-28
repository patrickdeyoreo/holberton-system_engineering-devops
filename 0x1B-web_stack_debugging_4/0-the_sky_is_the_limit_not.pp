# Increase file descriptor limit for NGINX

service {'nginx':
  ensure => running
}

exec {'sed -E -i \'s/^(ULIMIT=.*\<-n) [0-9]+\>/\1 1024/\' /etc/default/nginx':
  path   => '/usr/bin:/usr/sbin:/bin:/sbin',
  notify => Service['nginx']
}
