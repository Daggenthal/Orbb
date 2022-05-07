import sys, subprocess


def backup():
    while True:

            # Create a temporary directory that will be used throughout the script.
            subprocess.run(['mkdir /tmp/Backup/'], shell=True)

            print('\n\t NGINX settings, the mariaDB , and the postfix configs will be backed up.\n')
            print('\t Is this something you wanted to do?\n')
            print('\t 1: Yes')
            print('\t 2: No\n')

            response = str(input('\t Please input your selection: '))

            if response == '1':

                subprocess.run(['clear'], shell=True)
                print('\t Backup initiated, please wait...')

                # Start the backup process of the mariaDB database.
                subprocess.run(['cd /tmp/Backup/ && mysqldump --user=root --password=Admin1234! --lock-tables --all-databases > server_db_backup.sql'], shell=True)
                subprocess.run(['cd /tmp/Backup/ && tar -zcvf "TemporarydbBackup.tar.gz" server_db_backup.sql'], shell=True)
                subprocess.run(['cd /tmp/Backup/ && rm server_db_backup.sql'], shell=True)

                print('\n\t Backup has been completed, would you like to return to the main menu?\n')
                print('\t 1: Yes')
                print('\t 2: No')

                response = str(input('\t Please input your selection: '))

                if response == '1':
                    break
                elif response == '2':
                    sys.exit

            elif response == '2':
                break




def transferBackup():
    while True:
        subprocess.run([''], shell=True)
        
        response = str(input('\t Please input your selection: '))
        
        if response == '1':
            subprocess.run([''], shell=True)

        elif response == '2':
            break
        



def restoreBackup():
    while True:
        subprocess.run([''], shell=True)

        response = str(input('\t Please input your selection: '))

        if response == '1':
            subprocess.run([''], shell=True)

        elif response == '2':
            break




def return_to_loop():
	while True:
					
		print('\n\n ----------------------------------------------------------------------------\n')
		print('\t\t\t\t Orbb')
		print('\n\n\t Would you like to return to the main menu?\n\t')
		print('\t 1. Yes')
		print('\t 2. No')
		
		response = str(input('\n\t Response: '))
		if response == '1':
			break
		elif response == '2':
			subprocess.run(['clear'], shell=True)
			sys.exit() 				# This causes the program to terminate gracefully.
