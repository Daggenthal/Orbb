import sys, subprocess, time


def backup():
	while True:

			# Create a temporary directory that will be used throughout the script.

			subprocess.run(['mkdir /tmp/Backup/ && mkdir /tmp/Backup/etc/ && mkdir /tmp/Backup/usr'], shell=True)

			print('\n\t NGINX settings, the mariaDB database, letsencrypt SSL certs, \n\t and the postfix configs will be backed up.\n')
			print('\t Is this something you wanted to do?\n')
			print('\t 1: Yes')
			print('\t 2: No\n')

			response = str(input('\t Please input your selection: '))

			if response == '1':

				subprocess.run(['clear'], shell=True)
				print('\t Backup initiated, please wait, as this may take some time depending on your CPU speed...\n\t')

				# Start the backup process of the mariaDB database.

				subprocess.run(['cd /tmp/Backup/ && mysqldump --user=root --password=Admin1234! --lock-tables --all-databases > server_db_backup.sql'], shell=True)

				# Starts the backup process of my.cnf, NGINX, and postfix for the mail system / SendGrid settings, then moves them in the tmp directory.

				subprocess.run(['cp /etc/my.cnf /tmp/Backup/etc/'], shell=True)
				subprocess.run(['sudo cp -r /etc/nginx/ /tmp/Backup/etc/'], shell=True)
				subprocess.run(['sudo cp -r /etc/postfix/ /tmp/Backup/etc/'], shell=True)

				# Starts the backup process of the website, and its included files. This may take long depending on what's in there.

				subprocess.run(['sudo cp -r /usr/share/nginx/ /tmp/Backup/usr/'], shell=True)

				# Starts the backup process of the letsencrypt certs for the website's SSL

				subprocess.run(['sudo cp -r /etc/letsencrypt/ /tmp/Backup/etc/'], shell=True)

				# Compresses the /tmp/Backup/ folder for RSYNC later on.

				subprocess.run(['cd /tmp/ && sudo tar -zcvf "ServerBackup.tar.gz" /tmp/Backup '], shell=True)
				subprocess.run(['cd /tmp/ && sudo rm -rf Backup/'], shell=True)

				print('\n\t Backup has been completed, would you like to return to the main menu?\n')
				print('\t 1: Yes')
				print('\t 2: No\n')

				response = str(input('\t Please input your selection: '))

				if response == '1':
					break
				elif response == '2':
					subprocess.run(['clear'], shell=True)
					sys.exit()

			elif response == '2':
				break




def transferBackup():
	while True:
		
		#subprocess.run(['clear'], shell=True)
		print('\n\t This will RSYNC the Backup to the new server. Make sure to edit the IP \n\t in the script before you run this, otherwise it may not work.\n')
		print('\t Is this something you wanted to do?\n')
		print('\t 1: Yes')
		print('\t 2: No\n')
		
		response = str(input('\t Please input your selection: '))
		
		if response == '1':

			# This clears the terminal, and attempts to RSYNC the previously .tar.gz file we created earlier, and attempts to send it to the new one.
			# Please, if you use this, make sure to change out $yourUsername and $yourIP, otherwise it won't work at all.

			subprocess.run(['clear'], shell=True)

			# Here we're storing the target userName, and ipAddress, for the server where our file will be rsync'd to.
			# These will be called later on.

			userName = str(input('\n\t Please input the target username: '))
			ipAddress = str(input('\n\t Please input the target IP Address: '))

			subprocess.run(['clear'], shell=True)

			print('\n\t Are these correct?')
			print('\n\t Username: ', userName)
			print('\t IP Address: ', ipAddress, '\n')


			print('\t 1: Yes')
			print('\t 2: No\n')

			response = str(input('\t Please input your selection: '))

			if response == '1':

				subprocess.run(['clear'], shell=True)

				print('\n\t Attempting to rsync the file, please wait...\n\t')


				# Now we're going to take the input that we stored previously, and import them into the terminal command, so the user doesn't have to manually edit this source file.

				subprocess.run(['cd /tmp/ && sudo rsync ServerBackup.tar.gz', userName + '@' + ipAddress + ':/tmp/'], shell=True)

				print('\t Rsync was successful! Would you like to return to the main menu?\n')
				print('\t 1: Yes')
				print('\t 2: No\n')

				response = str(input('\t Please input your selection: '))

				if response == '1':
					break
				
				elif response == '2':
					subprocess.run(['clear'], shell=True)
					sys.exit()
					
			elif response == '2':
				
				subprocess.run(['clear'], shell=True)

				print('\n\t Returning to main menu...')

				time.sleep(1.25)

				break
			
		elif response == '2':
			break
		



def serverSetup():
	while True:
		
		subprocess.run(['clear'], shell=True)
		print('\n\t This will install the prerequisites that are needed. Do you want to proceed with this?\n')
		print('\t 1: Yes')
		print('\t 2: No\n')
				
		response = str(input('\t Please input your selection: '))

		if response == '1':
		
			# Here we're installing the necessary programs that we'll be using for later on. These are *required* for the restoreBackup() function to properly work.
			# What we're doing now is checking the users Linux distribution with 'cat /etc/os-release', and reading the output while scanning for key words, then executing what's needed.

			OS = subprocess.getoutput(['cat /etc/os-release'])
					
			if 'debian' in OS:
				subprocess.run(['sudo apt install -y nginx mariadb certbot postfix python3-certbot-nginx'], shell=True)
			elif 'ubuntu' in OS:
				subprocess.run(['sudo apt install -y nginx mariadb certbot postfix python3-certbox-nginx'], shell=True)
			elif 'fedora' in OS:
				subprocess.run(['sudo dnf install -y epel-release && sudo dnf install -y nginx mariadb certbot postfix python3-certbot-nginx'], shell=True)
			elif 'arch' in OS:
				subprocess.run(['sudo pacman -S --noconfirm nginx mariadb certbot postfix python3-certbot-nginx'], shell=True)
			elif 'opensuse' in OS:
				subprocess.run(['sudo zypper install -y nginx mariadb certbot postfix python3-certbot-nginx'], shell=True)
			elif 'freebsd' in OS:
				subprocess.run(['sudo pkg install -y nginx mariadb certbot postfix python3-certbot-nginx'], shell=True)
			
			print('\t The prerequisites have been installed! Would you like to return to the main menu?\n')

			response = str(input('\t Please input your selection: '))

			if response == '1':
				break
			elif response == '2':
				subprocess.run(['clear'], shell=True)
				sys.exit()
  
		elif response == '2':
			break




def restoreBackup():
	while True:
		
		subprocess.run(['clear'], shell=True)
		print('\n\t Please make sure you have the pre-requisites installed! \n\t In this case, you need NGINX, mariaDB, certbot, and postfix.\n')
		print('\n\t Please make sure that mariDB is properly setup\n\t with the corresponding user that you will use.\n')
		print('\n\t Do you want to proceed with this?\n')
		print('\t 1: Yes')
		print('\t 2: No\n')

		response = str(input('\t Please input your selection: '))

		if response == '1':

			# This CD's into /tmp/ and untar's our .tar.gz that we created earlier.
			# Please, make sure that you're in the proper folder in order for this to work.



			subprocess.run(['clear'], shell=True)
			
			# Here we're going to disable the services while we attempt to restore them.

			print('\t Disabling services momentarily...')
			subprocess.run(['sudo systemctl stop nginx'], shell=True)
			subprocess.run(['sudo systemctl stop postfix'], shell=True)
			subprocess.run(['sudo systemctl stop mariadb'], shell=True)
			print('\t Services have successfully been disabled. Attempting restoration, please wait...\n\t')

			# Here we're beginning to decompress the file we created, and moved, earlier. This contains everything we need to properly setup the new server.

			print('\t Attempting to decompress the file, please wait...\n\t')
			subprocess.run(['cd /tmp/ && sudo tar xvzf ServerBackup.tar.gz'], shell=True)
			print('\t The file has successfully been decompressed! Attempting restore...\n\t')

			# Here we're going to move the files to the proper directory that they came from.
			# These 3 lines move our /etc/ files back to their origin.

			subprocess.run(['cd /tmp/tmp/Backup/etc && sudo mv my.cnf /etc/'], shell=True)
			subprocess.run(['cd /tmp/tmp/Backup/etc && sudo mv nginx/ /etc/'], shell=True)
			subprocess.run(['cd /tmp/tmp/Backup/etc && sudo mv postfix /etc/'], shell=True)
			print('\t /etc/ folders have successfully been restored. Attempting website restore...\n\t')

			# Now we're going to move the website and mail certs back to their origin.

			subprocess.run(['cd /tmp/tmp/Backup/usr && sudo mv nginx/ /usr/share/nginx'], shell=True)
			print('\t Website has successfully been restored! Attempting API key restore...\n\t')

			# Now we're going to setup postfix so we can use the same API keys

			subprocess.run(['sudo postmap /etc/postfix/sasl_passwd'], shell=True)
			print('\t API keys have been successfully restored. Attempting SSL certs restore...\n')

			# Now we're going to restore the letsencrypt SSL certificates for the website.
			
			subprocess.run(['cd /tmp/tmp/Backup/etc && sudo mv letsencrypt/ /etc/'], shell=True)
			print('\t SSL certs have successfully been restored!\n')

			# Now we'll start the services again, and enable them to persist upon reboot.

			print('\n\t Starting services, and enabling them for future reboots, please wait...\n\t')
			subprocess.run(['sudo systemctl start nginx && sudo systemctl enable nginx'], shell=True)
			subprocess.run(['sudo systemctl start postfix && sudo systemctl enable postfix'], shell=True)
			subprocess.run(['sudo systemctl start mariadb && sudo systemctl enable mariadb'], shell=True)
			
			print('\t Services have successfully been enabled! Would you like to return to the main menu?\n\t')
			print('\t 1: Yes')
			print('\t 2: No\n')

			response = str(input('\t Please input your selection: '))

			if response == '1':
				break
			elif response == '2':
				subprocess.run(['clear'], shell=True)
				sys.exit()


		elif response == '2':
			break
