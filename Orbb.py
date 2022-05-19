import sys, functions

from subprocess import run

try: 
        while True:

                run(['clear'], shell=True)
                print('\t Welcome to Orbb! What would you like to do? \n')
                print('\t 1: Backup')
                print('\t 2: Transfer Backup')
                print('\t 3: Server Setup')
                print('\t 4: Restore Backup')
                print('\t 5: Exit \n')

                response = str(input('\t Please input your selection as a number: '))
                run(['clear'], shell=True)
                if response == '1':
                        functions.backup()
                elif response == '2':
                        functions.transferBackup()
                elif response == '3':
                        functions.serverSetup()
                elif response == '4':
                        functions.restoreBackup()
                elif response == '5':
                        sys.exit()

except KeyboardInterrupt:
        run(['clear'], shell=True)
        print('User has purposefully interrupted the execution of the program.')
