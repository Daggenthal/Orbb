from re import sub
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
                print('\t Backup initiated, please wait, as this may take some time depending on your CPU speed...\n\t')

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
        
        subprocess.run(['clear'], shell=True)
        print('\n\t This will RSYNC the Backup to the new server. Make sure to enter the IP before you run this, otherwise it may not work.\n')
        print('\t Is this something you wanted to do?\n')
        print('\t 1: Yes')
        print('\t 2: No\n')
        
        response = str(input('\t Please input your selection: '))
        
        if response == '1':

            # This clears the terminal, and attempts to RSYNC the previously .tar.gz file we created earlier, and attempts to send it to the new one.
            # Please, if you use this, make sure to change out $yourUsername and $yourIP, otherwise it won't work at all.

            subprocess.run(['clear'], shell=True)
            print('\t Attempting to rsync the file, please wait...\n\t')

            subprocess.run(['cd /tmp/ && rsync ServerBackup.tar.gz USER@IP:/tmp/'], shell=True)
            print('\t Rsync was successful! Would you like to return to the main menu?\n')

            response = str(input('\t Please input your selection: '))

            if response == '1':
                break
            elif response == '2':
                sys.exit()

        elif response == '2':
            break
        



def restoreBackup():
    while True:
        
        subprocess.run(['clear'], shell=True)
        print('\n\t Please make sure you have the pre-requisites installed! In this case, you need NGINX, mariaDB, and postfix.\n')
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

            subprocess.run(['cd /tmp/Backup/etc && sudo mv my.cnf /etc/'], shell=True)
            subprocess.run(['cd /tmp/Backup/etc && sudo mv nginx/ /etc/'], shell=True)
            subprocess.run(['cd /tmp/Backup/etc && sudo mv postfix /etc/'], shell=True)
            print('\t /etc/ folders have successfully been restored. Attempting website restore...\n\t')

            # Now we're going to move the website and mail certs back to their origin.

            subprocess.run(['cd /tmp/Backup/usr && sudo mv nginx/ /usr/share/nginx'], shell=True)
            print('\t Website has successfully been restored! Attempting API key restore...\n\t')

            # Now we're going to setup postfix so we can use the same API keys

            subprocess.run(['sudo postmap /etc/postfix//sasl_passwd'], shell=True)
            print('\t API keys have been successfully restored!\n')

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
                sys.exit()


        elif response == '2':
            break
