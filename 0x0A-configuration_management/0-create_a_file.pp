# Create a file

file { '/tmp/holberton':
  ensure  => 'present',
  replace => 'no',
  group   => 'www-data',
  owner   => 'www-data',
  mode    => '0644',
  content => "I love Puppet\n",
}
