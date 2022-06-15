from subprocess import getoutput

OS = getoutput(["cat /etc/os-release | awk 'NR==3'"])

#############################################################################################################################################################

distro = ['debian', 'ubuntu', 'fedora', 'rocky', 'arch', 'opensuse', 'freebsd']

debian = 'sudo apt install -y nginx mariadb-server memcached certbot postfix pv php-cli php-fpm python3-certbot-nginx'

fedora = 'sudo dnf install -y nginx mariadb-server memcached certbot postfix pv php-cli php-fpm python3-certbot-nginx'

rocky = 'sudo dnf install -y epel-release && sudo dnf install -y nginx mariadb-server memcached certbot postfix pv php-cli php-mysqli php-xml php-fpm python3-certbot-nginx'

arch = 'sudo pacman -S --noconfirm nginx mariadb-server memcached certbot postfix pv php-cli php-fpm python3-certbot-nginx'

opensuse = 'sudo zypper install -y nginx mariadb-server memcached certbot postfix pv php-cli php-fpm python3-certbot-nginx'

freebsd = 'sudo pkg install nginx mariadb106-server-10.6.8 mariadb106-client-10.6.8  memcached postfix py38-certbot-nginx-1.22.0 apache24-2.4.54'

#############################################################################################################################################################

dpv = 'sudo apt install -y pv'

fpv = 'sudo dnf install -y pv'

apv = 'sudo pacman -S --noconfirm pv'

opv = 'sudo zypper install -y pv'

bpv = 'sudo pkg install -y pv'
