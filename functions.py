from subprocess import run, getoutput
from sys import exit
from time import sleep


def Backup():
	while True:

			# Create a temporary directory that will be used throughout the script.

			run(['mkdir /tmp/Backup/ && mkdir /tmp/Backup/etc/ && mkdir /tmp/Backup/usr'], shell=True, check=True)

			print('\n\t NGINX settings, the mariaDB database, letsencrypt SSL certs, \n\t and the postfix configs will be backed up.\n')
			print('\t Is this something you wanted to do?\n')
			print('\t 1: Yes')
			print('\t 2: No\n')

			response = input('\t Please input your selection: ')

			if response == '1':

				run(['clear'], shell=True)

				print('\t Backup initiated, please wait, as this may take some time depending on your CPU speed...\n\t')

				# Start the backup process of the mariaDB database.

				run(['cd /tmp/Backup/ && mysqldump --user=root --password=Admin1234! --lock-tables --all-databases > server_db_backup.sql'], shell=True, check=True)

				# Starts the backup process of my.cnf, NGINX, and postfix for the mail system / SendGrid settings, then moves them in the tmp directory.

				run(['cp /etc/my.cnf /tmp/Backup/etc/'], shell=True, check=True)
				run(['sudo cp -r /etc/nginx/ /tmp/Backup/etc/'], shell=True, check=True)
				run(['sudo cp -r /etc/postfix/ /tmp/Backup/etc/'], shell=True, check=True)

				# Starts the backup process of the website, and its included files. This may take long depending on what's in there.

				run(['sudo cp -r /usr/share/nginx/ /tmp/Backup/usr/'], shell=True, check=True)

				# Starts the backup process of the letsencrypt certs for the website's SSL

				run(['sudo cp -r /etc/letsencrypt/ /tmp/Backup/etc/'], shell=True, check=True)

				# Compresses the /tmp/Backup/ folder for RSYNC later on.

				run(['cd /tmp/ && sudo tar -zcvf "ServerBackup.tar.gz" /tmp/Backup '], shell=True, check=True)
				run(['cd /tmp/ && sudo rm -rf Backup/'], shell=True, check=True)

				print('\n\t Backup has been completed, would you like to return to the main menu?\n')
				print('\t 1: Yes')
				print('\t 2: No\n')

				response = input('\t Please input your selection: ')

				if response == '1':
					break
				elif response == '2':
					run(['clear'], shell=True)
					exit()

			elif response == '2':
				break




def transferBackup():
	while True:
		
		run(['clear'], shell=True)

		print('\n\t This will RSYNC the Backup to the new server.\n')
		print('\t Is this something you wanted to do?\n')
		print('\t 1: Yes')
		print('\t 2: No\n')
		
		response = input('\t Please input your selection: ')
		
		if response == '1':

			# This clears the terminal, and attempts to RSYNC the previously .tar.gz file we created earlier, and attempts to send it to the new one.
			# Please, if you use this, make sure to change out $yourUsername and $yourIP, otherwise it won't work at all.

			run(['clear'], shell=True)

			# Here we're storing the target userName, and ipAddress, for the server where our file will be rsync'd to.
			# These will be called later on.

			userName = input('\n\t Please input the target username: ')
			ipAddress = input('\n\t Please input the target IP Address: ')

			run(['clear'], shell=True)

			print('\n\t Are these correct?')
			print('\n\t Username: ', userName)
			print('\t IP Address: ', ipAddress, '\n')


			print('\t 1: Yes')
			print('\t 2: No\n')

			response = input('\t Please input your selection: ')

			if response == '1':

				run(['clear'], shell=True)

				print('\n\t Attempting to rsync the file, please wait...\n\t')


				# Now we're going to take the input that we stored previously, and import them into the terminal command, so the user doesn't have to manually edit this source file.

				run(['cd /tmp/ && sudo rsync -v ServerBackup.tar.gz', userName + '@' + ipAddress + ':/tmp/'], shell=True, check=True)

				print('\t Rsync was successful! Would you like to return to the main menu?\n')
				print('\t 1: Yes')
				print('\t 2: No\n')

				response = input('\t Please input your selection: ')

				if response == '1':
					break
				
				elif response == '2':
					run(['clear'], shell=True)
					exit()
					
			elif response == '2':
				run(['clear'], shell=True)
				print('\n\t Returning to main menu...')
				sleep(1.25)
				break
			
		elif response == '2':
			break
		



def serverSetup():
	while True:
		
		run(['clear'], shell=True)

		print('\n\t This will install the prerequisites that are needed. Do you want to proceed with this?\n')
		print('\t 1: Yes')
		print('\t 2: No\n')
				
		response = input('\t Please input your selection: ')

		if response == '1':
		
			# Here we're installing the necessary programs that we'll be using for later on. These are *required* for the restoreBackup() function to properly work.
			# What we're doing now is checking the users Linux distribution with 'cat /etc/os-release', and reading the output while scanning for key words, then executing what's needed.

			OS = getoutput(['cat /etc/os-release'])
					
			if 'debian' in OS:
				run(['sudo apt install -y nginx mariadb-server certbot postfix python3-certbot-nginx'], shell=True, check=True)
			elif 'ubuntu' in OS:
				run(['sudo apt install -y nginx mariadb-server certbot postfix python3-certbox-nginx'], shell=True, check=True)
			elif 'fedora' in OS:
				run(['sudo dnf install -y epel-release && sudo dnf install -y nginx mariadb-server certbot postfix python3-certbot-nginx'], shell=True, check=True)
			elif 'arch' in OS:
				run(['sudo pacman -S --noconfirm nginx mariadb-server certbot postfix python3-certbot-nginx'], shell=True, check=True)
			elif 'opensuse' in OS:
				run(['sudo zypper install -y nginx mariadb-server certbot postfix python3-certbot-nginx'], shell=True, check=True)
			elif 'freebsd' in OS:
				run(['sudo pkg install -y nginx mariadb-server certbot postfix python3-certbot-nginx'], shell=True, check=True)
			
			print('\n\t The prerequisites have been installed! Would you like to return to the main menu?\n')
			print('\t 1: Yes')
			print('\t 2: No\n')

			response = input('\t Please input your selection: ')

			if response == '1':
				break
			elif response == '2':
				run(['clear'], shell=True)
				exit()
  
		elif response == '2':
			break




def restoreBackup():
	while True:
		
		run(['clear'], shell=True)

		print('\n\t Please make sure you have the pre-requisites installed! \n\t In this case, you need NGINX, mariaDB, certbot, and postfix.\n')
		print('\n\t Please make sure that mariDB is properly setup\n\t with the corresponding user that you will use.\n')
		print('\n\t Do you want to proceed with this?\n')
		print('\t 1: Yes')
		print('\t 2: No\n')

		response = input('\t Please input your selection: ')

		if response == '1':

			# This CD's into /tmp/ and untar's our .tar.gz that we created earlier.
			# Please, make sure that you're in the proper folder in order for this to work.



			run(['clear'], shell=True)
			
			# Here we're going to disable the services while we attempt to restore them.

			print('\t Disabling services momentarily...')

			run(['sudo systemctl stop nginx'], shell=True, check=True)
			run(['sudo systemctl stop postfix'], shell=True, check=True)
			run(['sudo systemctl stop mariadb'], shell=True, check=True)

			print('\t Services have successfully been disabled. Attempting restoration, please wait...\n\t')

			# Here we're beginning to decompress the file we created, and moved, earlier. This contains everything we need to properly setup the new server.

			print('\t Attempting to decompress the file, please wait...\n\t')

			run(['cd /tmp/ && sudo tar xvzf ServerBackup.tar.gz'], shell=True, check=True)

			print('\t The file has successfully been decompressed! Attempting restore...\n\t')

			# Here we're going to move the files to the proper directory that they came from.
			# These 4 lines move our /etc/ files back to their origin, with the first one moving my.cnf so we can properly complete the restore.

			run(['cd /tmp/tmp/Backup/etc && sudo cp my.cnf /etc/'], shell=True, check=True)
			run(['cd /tmp/tmp/Backup/etc && sudo cp -r nginx/ /etc/'], shell=True, check=True)
			run(['cd /tmp/tmp/Backup/etc && sudo cp -r postfix/ /etc/'], shell=True, check=True)

			print('\t /etc/ folders have successfully been restored. Attempting website restore...\n\t')

			# Now we're going to move the website and mail certs back to their origin.

			run(['cd /tmp/tmp/Backup/usr && sudo cp -r nginx/ /usr/share/'], shell=True, check=True)

			print('\t Website has successfully been restored! Attempting API key restore...\n\t')

			# Now we're going to setup postfix so we can use the same API keys

			run(['sudo postmap /etc/postfix/sasl_passwd'], shell=True, check=True)

			print('\t API keys have been successfully restored. Attempting SSL certs restore...\n')

			# Now we're going to restore the letsencrypt SSL certificates for the website.
			
			run(['cd /tmp/tmp/Backup/etc && sudo cp -r letsencrypt/ /etc/'], shell=True, check=True)

			print('\t SSL certs have successfully been restored!\n')

			# Now we'll start the services again, and enable them to persist upon reboot.

			print('\t Have you already setup MariaDB?\n')
			print('\t 1: Yes')
			print('\t 2: No\n')

			response = input('\t Please input your selection: ')

			if response == '1':
				userName = input('\n\t Please enter the username: ')
				passWord = input('\n\t Please enter the password: ')

				print('\n\t Attempting mariaDB / mySQL Database restoration, please wait... ')
				run(['sudo mysql --user ' + userName + ' --password ' + passWord + ' --force < /tmp/tmp/Backup/server_db_backup.sql'], shell=True, check=True)
				print('\n\t Database restoration was successful! Completing restoration, please wait... ')
				sleep(1.25)
				
			elif response == '2':
				print('\t Would you like to go ahead and setup MariaDB?\n')
				print('\t 1: Yes')
				print('\t 2: No\n')

				if response == '1':
					run(['sudo mysql_secure_installation'], shell=True, check=True)

					userName = input('\n\t Please enter the username: ')
					passWord = input('\n\t Please enter the password: ')

					print('\n\t Attempting mariaDB / mySQL Database restoration, please wait... ')
					run(['sudo mysql --user ' + userName + ' --password ' + passWord + ' --force < /tmp/tmp/Backup/server_db_backup.sql'], shell=True, check=True)
					print('\n\t Database restoration was successful! Completing restoration, please wait... ')
					sleep(1.25)

				elif response == '2':
					print('\n\t Please note, that you may need to manually\n\t setup the DB for it to properly function.')
					print('\n\n\t Continuing restoration, please wait...')
					sleep(3)
					break

			print('\n\t Starting services, and enabling them for future reboots, please wait...\n')

			run(['sudo systemctl start nginx && sudo systemctl enable nginx'], shell=True, check=True)
			run(['sudo systemctl start postfix && sudo systemctl enable postfix'], shell=True, check=True)
			run(['sudo systemctl start mariadb && sudo systemctl enable mariadb'], shell=True, check=True)
			
			print('\t Services have successfully been enabled! Would you like to return to the main menu?\n')
			print('\t 1: Yes')
			print('\t 2: No\n')

			response = input('\t Please input your selection: ')

			if response == '1':
				break
			elif response == '2':
				run(['clear'], shell=True)
				exit()


		elif response == '2':
			break
