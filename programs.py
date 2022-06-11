from subprocess import getoutput

OS = getoutput(['cat /etc/os-release'])

#############################################################################################################################################################

distro = ['debian', 'ubuntu', 'fedora', 'arch', 'opensuse', 'freebsd']

debian = 'sudo apt install -y nginx mariadb-server memcached certbot postfix pv php-cli python3-certbot-nginx httpd'

ubuntu = 'sudo apt install nginx mariadb-server memcached certbot postfix pv php-cli python3-certbox-nginx httpd'

fedora = 'sudo dnf install -y epel-release && sudo dnf install -y nginx mariadb-server memcached certbot postfix pv php-cli python3-certbot-nginx httpd'

arch = 'sudo pacman -S --noconfirm nginx mariadb-server memcached certbot postfix pv php-cli python3-certbot-nginx httpd'

opensuse = 'sudo zypper install -y nginx mariadb-server memcached certbot postfix pv php-cli python3-certbot-nginx httpd'

freebsd = 'sudo pkg install -y nginx mariadb106-server-10.6.8 memcached postfix py38-certbot-nginx-1.22.0 apache24-2.4.53_1'

#############################################################################################################################################################

dpv = 'sudo apt install -y pv'

upv = 'sudo apt install -y pv'

fpv = 'sudo dnf install -y pv'

apv = 'sudo pacman -S --noconfirm pv'

opv = 'sudo zypper install -y pv'

bpv = 'sudo pkg install -y pv'