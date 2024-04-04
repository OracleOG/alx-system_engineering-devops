file { '~/.ssh/config':
  ensure  => file,
  mode    => '0600',
  content => "
Host ubuntu
    IdentityFile ~/.ssh/school
    PasswordAuthentication no
",
}