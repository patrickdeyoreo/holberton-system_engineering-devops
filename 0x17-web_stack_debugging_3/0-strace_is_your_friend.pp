# Debug th web stack

file {'new':
  path   => '/var/www/html/wp-includes/class-wp-locale.phpp',
  ensure => file,
  source => '/var/www/html/wp-includes/class-wp-locale.php',
  after  => File['old']
}

file {'old':
  path   => '/var/www/html/wp-includes/class-wp-locale.php',
  ensure => absent
}
