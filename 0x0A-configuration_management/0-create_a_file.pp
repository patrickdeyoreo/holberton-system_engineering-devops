# Create a file

file { '/tmp/holberton':
  ensure  => 'present',
  replace => 'no',
  group   => 'www-data',
  owner   => 'www-data',
  mode    => '0744',
  content => "I love Puppet\n",
}
