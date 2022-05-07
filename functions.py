import sys, subprocess


def backup():
    while True:

            subprocess.run(['mkdir /tmp/Backup/ && cd /tmp/Backup/'], shell=True)

            print('\n\t NGINX settings, the mariaDB, and the postfix configs will be backed up.\n')
            print('\t Is this something you wanted to do?')
            print('\t 1: Yes')
            print('\t 2: No')

            response = str(input('\t Please input your selection: '))

            if response == '1':
                subprocess.run(['mysqldump --user=root --password=Admin1234! --lock-tables --all-databases > server_db_backup.sql'], shell=True)
                subprocess.run(['tar -zcvf "$(date '+%Y-%m-%d').tar.gz" server_db_backup.sql'], shell=True)
                subprocess.run(['rm server_db_backup.sql'], shell=True)
            elif response == '2':
                break
