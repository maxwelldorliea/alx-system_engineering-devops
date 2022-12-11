# make changes to our configuration file

file_line {'password-less':
path    => '/etc/ssh/ssh_config',
line    => '    PasswordAuthentication no',
replace => True
}


file_line {'private-key':
path    => '/etc/ssh/ssh_config',
line    => '    IdentityFile ~/.ssh/school',
replace => True
}
