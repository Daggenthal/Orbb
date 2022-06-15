from subprocess import getoutput

OS = getoutput(["cat /etc/os-release | awk 'NR==3'"])

#############################################################################################################################################################

distro = ['debian', 'ubuntu', 'fedora', 'rocky', 'arch', 'opensuse', 'freebsd']

debian = 'sudo apt install -y nginx mariadb-server memcached certbot postfix pv php-cli python3-certbot-nginx httpd'

fedora = 'sudo dnf install -y nginx mariadb-server memcached certbot postfix pv php-cli python3-certbot-nginx httpd'

rocky = 'sudo dnf install -y epel-release && sudo dnf install -y nginx mariadb-server memcached certbot postfix pv php-cli python3-certbot-nginx httpd'

arch = 'sudo pacman -S --noconfirm nginx mariadb-server memcached certbot postfix pv php-cli python3-certbot-nginx httpd'

opensuse = 'sudo zypper install -y nginx mariadb-server memcached certbot postfix pv php-cli python3-certbot-nginx httpd'

freebsd = 'sudo pkg install nginx mariadb106-server-10.6.8 mariadb106-client-10.6.8  memcached postfix py38-certbot-nginx-1.22.0 apache24-2.4.54'

#############################################################################################################################################################

dpv = 'sudo apt install -y pv'

fpv = 'sudo dnf install -y pv'

apv = 'sudo pacman -S --noconfirm pv'

opv = 'sudo zypper install -y pv'

bpv = 'sudo pkg install -y pv'
