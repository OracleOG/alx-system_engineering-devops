# Install the Flask package.

# Include the python module to ensure Python is available
include python

# Define a class for installing flask with pip3
class { 'flask_install':
  # Ensure flask package is installed with pip3 and specify version
  package { 'flask':
    ensure => installed,
    provider => 'pip3',
    require => Class['python'],
    version => '2.1.0',
  }
}
