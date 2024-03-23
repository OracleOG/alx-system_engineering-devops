# Install the Flask package.
exec { 'install_flask':
  command     => '/usr/bin/pip3 install Flask==2.1.0',
  path        => ['/usr/bin', '/usr/local/bin'], # Add necessary paths
  refreshonly => true, # Only run if notified to refresh
}
