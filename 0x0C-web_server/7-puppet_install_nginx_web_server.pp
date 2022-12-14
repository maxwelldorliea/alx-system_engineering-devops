# perform a 301 redirect when querying /redirect_me.

# exec {'update host':
# command => '/usr/bin/apt update -y'
# }

# exec {'upgrade host':
# command => '/usr/bin/apt upgrade -y'
# }

exec {'Install nginx':
command => '/usr/bin/apt install nginx'
}

exec {'Change var www owner':
command => '/usr/bin/chown -R $USER:$USER /var/www'
}

exec {'Make Homepage to display hello world':
command => '/usr/bin/echo Hello World > /var/www/html/index.nginx-debian.html'
}

file_line {'redirect permanently':
path    => '/etc/nginx/sites-available/default',
line  => 'rewrite ^/redirect_me/$ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
after   => 'root /var/www/html;',
replace => true
}
