class init {
    exec { "apt-update":
        command => "/usr/bin/apt-get update",
        timeout => 0,
    }

    Exec["apt-update"] -> Package <| |>

    class { 'postgresql::globals':
      encoding => 'UTF-8',
      locale   => 'en_US.UTF-8',
    }->
    class { 'postgresql::server': }

    postgresql::server::db { 'drood':
      user     => 'drood',
      password => postgresql_password('drood', 'drood'),
    }

    package {
        ['build-essential', 'python', 'python-dev', 'python-virtualenv', 'libevent-dev', 'libpq-dev', 'libmemcached-dev', 'zlib1g-dev', 'libssl-dev', 'python-pip', 'libjpeg-dev']:
        ensure => 'installed',
        require => Exec['apt-update'] # The system update needs to run first
    }

    exec { "pip-install-requirements":
        cwd => "/vagrant",
        command => "/usr/bin/pip install -r /vagrant/drood/requirements/local.txt",
        tries => 2,
        user => root,
        timeout => 0,
        require => Package['python-pip', 'python-dev', 'libjpeg-dev', 'build-essential'],
        logoutput => on_failure,
    }
}
