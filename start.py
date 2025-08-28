import sys,os
from colorama import Fore

print(Fore.MAGENTA+"""
――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
 _______  _______  _______  _______         _______ __________________ _______  _______  _        _______  ______    
/ ___   )(  ____ \(  ____ )(  ___  )       (  ___  )\__   __/\__   __/(  ___  )(  ____ \| \    /\(  ____ \(  ____ )  
\/   )  || (    \/| (    )|| (   ) |       | (   ) |   ) (      ) (   | (   ) || (    \/|  \  / /| (    \/| (    )|  
    /   )| (__    | (____)|| |   | | _____ | (___) |   | |      | |   | (___) || |      |  (_/ / | (__    | (____)|
   /   / |  __)   |     __)| |   | |(_____)|  ___  |   | |      | |   |  ___  || |      |   _ (  |  __)   |     __)
  /   /  | (      | (\ (   | |   | |       | (   ) |   | |      | |   | (   ) || |      |  ( \ \ | (      | (\ (   
 /   (_/\| (____/\| ) \ \__| (___) |       | )   ( |   | |      | |   | )   ( || (____/\|  /  \ \| (____/\| ) \ \__
(_______/(_______/|/   \__/(_______)       |/     \|   )_(      )_(   |/     \|(_______/|_/    \/(_______/|/   \__/
                                                                                                                   
――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
                                                                
       """)


print(Fore.RED + 'recoded and recreated by @imtheisobhan on Telgram')


def display_menu():
    print(Fore.GREEN + """
    1: Zero-Tool (Hacking Tools) 
    2: option deleted 
    3: option deleted
    """)

def execute_command(command):
    if command == '1':
        os.system('cmd /k "python ZeroScrip/zero-tool.py"' if os.name == 'nt' else 'python ZeroScrip/zero-tool.py')
    elif command == '2':
        print(Fore.RED + 'option deleted ')
    elif command == '3':
        print(Fore.BLACK + 'option deleted')

        display_menu()
    else:
        print('invailed CMD !!! ')

while True:
    display_menu()
    command = input('> ')

    if command.lower() == 'exit':
        break

    execute_command(command)
