# Kills a process called kill me now.
exec { 'kill_killmenow_process':
  command => '/usr/bin/pkill killmenow',
  path    => '/usr/bin',
  onlyif  => '/usr/bin/pgrep -x killmenow',
}
