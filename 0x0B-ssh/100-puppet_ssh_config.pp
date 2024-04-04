# automates the config process

file { '/etc/ssh/ssh_config':
  ensure  => file,
  mode    => '0600',
  content => "
Host ubuntu
    IdentityFile ~/.ssh/school
    PasswordAuthentication no
",
}