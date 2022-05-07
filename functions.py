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
                print('\t Backup initiated, please wait, as this is running...\n\t')

                # Start the backup process of the mariaDB database.
                subprocess.run(['cd /tmp/Backup/ && mysqldump --user=root --password=Admin1234! --lock-tables --all-databases > server_db_backup.sql'], shell=True)

                # Starts the backup process of my.cnf, NGINX, and postfix for the mail system / SendGrid settings, then moves them in the tmp directory.
                subprocess.run(['mkdir /tmp/Backup/etc/'], shell=True)
                subprocess.run(['cp /etc/my.cnf /tmp/Backup/etc/'], shell=True)
                subprocess.run(['sudo cp -r /etc/nginx/ /tmp/Backup/etc/'], shell=True)
                subprocess.run(['sudo cp -r /etc/postfix/ /tmp/Backup/etc/'], shell=True)

                # Starts the backup process of the website, and its included files. This may take long depending on what's in there.
                subprocess.run(['mkdir /tmp/Backup/usr'], shell=True)
                subprocess.run(['sudo cp -r /usr/share/nginx/ /tmp/Backup/usr/'], shell=True)

                # Compresses the /tmp/Backup/ folder for RSYNC later on.
                subprocess.run(['cd /tmp/ && tar -zcvf "ServerBackup.tar.gz" /tmp/Backup/ '], shell=True)
                subprocess.run(['cd /tmp/ && sudo rm -rf Backup/'], shell=True)

                print('\n\t Backup has been completed, would you like to return to the main menu?\n')
                print('\t 1: Yes')
                print('\t 2: No\n')

                response = str(input('\t Please input your selection: '))

                if response == '1':
                    break
                elif response == '2':
                    sys.exit()

            elif response == '2':
                break




def transferBackup():
    while True:
        
        subprocess.run(['clear'], shell=True)
        print('\n\t This will RSYNC the Backup to the new server. Make sure to enter the IP before you run this, otherwise it may not work.\n')
        print('\t Is this something you wanted to do?\n')
        print('\t 1: Yes')
        print('\t 2: No\n')
        
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
