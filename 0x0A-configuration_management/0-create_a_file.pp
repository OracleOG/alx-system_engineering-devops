# This Manifest creates a file with name 'school' in the /tmp/ directory
file{'/tmp/school/':
ensure  => file,
mode    => '0744',
owner   => 'www-data',
group   => 'www-data',
content => 'I love puppet',
}
