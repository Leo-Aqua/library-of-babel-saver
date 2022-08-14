import os
while True:
    os.system('cls')
    print('''

    888b.      8          8 
    8wwwP .d88 88b. .d88b 8 
    8   b 8  8 8  8 8.dP' 8 
    888P' `Y88 88P' `Y88P 8 
                           Main
                        
        [1] Generate
        [2] Read
        [3] Exit
        ''')
    choice = input('>> ')
    if choice == '1':
        
        try:
            os.system('gen.py')
        except KeyboardInterrupt:
            pass
    elif choice == '2':
        
        try:
            os.system('read.py')
        except KeyboardInterrupt:
            pass
    elif choice == '3':
        break
    else:
        print('Invalid Option')
        input('Press Enter to continue')
        os.system('cls')