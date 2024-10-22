#!/usr/bin/env python3

import string
import secrets
import datetime

is_running = True #Boolean to control the running loop.

def gen_pass(size, cap, nums, spcs): #Defining a specific function to generate the password instead of hardcoding it into the main one makes the code cleaner.
    chars = ''

    if cap == 'a':
        chars += string.ascii_letters
    elif cap == 'u':
        chars += string.ascii_uppercase
    elif cap == 'l':
        chars += string.ascii_lowercase

    if nums == 'usenums':
        chars += string.digits
    elif nums == 'pass':
        pass

    if spcs == 'usespcs':
        chars += string.punctuation
    elif spcs == 'pass':
        pass

    password = ''
    for _ in range(size):
        password += ''.join(secrets.choice(chars)) #Randomly chooses characters from 'chars' variable and adds them to the 'password' variable as many times as the integer defined as 'size'.
    return password

def get_help():
        print('The software takes a command line with one command \'generate\' plus four parameters:\n' )
        print('1. Specifies how many characters the password will have, must be an integer number;')
        print('2. Defines the letters in the password: \'u\' for uppercase, \'l\' for lowercase and \'a\' for both;')
        print('3. Defines the use of numerical digits from 0 to 9, insert \'usenums\' to include them or \'pass\' to ignore this parameter;')
        print('4. Defines the use of special and puctuation characters, insert \'usespcs\' to include them or \'pass\' to ignore this parameter.\n')
        print('If you wish to close the program, insert \'exit\' and press enter.')
        print('If you need help, insert \'help\' and press enter.\n')

def run_soft(): #Main function that controls the flow of other functions, including the one that generates the password. Makes the code more organized.

    print('Welcome to PassGen 1.0, a simple and secure password generator.')
    print('The basic synthax is: \'generate [size] [cap] [nums] [spcs]\'')

    while True: #Loop to prevent crashes due to wrong command lines.

        try:

            comm = input('\nInsert command: ').split() #Creates a list from the command inserted by user, makes it easier to control the flow of the code.

            if (comm[0] in ['exit', 'help']) or (comm[0] == 'generatre' and isinstance(int(comm[1]), int) and comm[2] in ['a', 'u', 'l'] and comm[3] in ['usenums', 'pass'] and comm[4] in ['usespcs', 'pass']):
                break

            else:

                if comm[0] not in ['generate', 'exit', 'help']:
                    print(f'\'{comm[0]}\' is not a valid command.')

                elif comm[2] not in ['a', 'u', 'l']:
                    print(f'\'{comm[2]}\' is not a valid parameter.')

                elif comm[3] not in ['usenums', 'pass']:
                    print(f'\'{comm[3]}\' is not a valid parameter.')

                elif comm[4] not in ['usespcs', 'pass']:
                    print(f'\'{comm[4]}\' is not a valid parameter.')


        except ValueError:
            print('Your command line contains one or more values of the wrong type. If you need help, insert \'help\' and press enter.')
        except IndexError:
            print('Your command line contains empty parameters, try again.')

    if comm[0] == 'exit':
        global is_running
        is_running = False

    elif comm[0] == 'help':
        get_help()

    else:

        password = gen_pass(int(comm[1]), comm[2], comm[3], comm[4])

        with open('pass_gen_entries.txt', 'a') as pge:
            pge.write(f'{password} ({datetime.datetime.now()})\n') #Writes the password in a text file for future uses, along with date and time when it was generated.

        print(f'\nPassword generated: \'{password}\'. Access it at /PassGen1.0/pass_gen_entries.txt.\n')

while is_running: #Running loop controlled by boolean is_running.
    run_soft()
