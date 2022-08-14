import os
import win32clipboard

def text():
    os.system('cls')
    name = input('Name:\n')
    os.system('cls')
    
    print('Using Clipboard for Location...')
    input('Press Enter to continue')
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    os.system('cls')

    wall = input('Wall:\n')
    os.system('cls')
    shelf = input('Shelf:\n')
    os.system('cls')
    vol = input('Volume:\n')
    os.system('cls')
    page = input('Page:\n')
    os.system('cls')
    if len(vol) == 1:
        vol = f'0{vol}'
    else:
        pass

    #content = str('data' + ';;' + 'wall' + ';;' + 'shelf' + ';;' + 'vol' + ';;' + 'page')

    content = str(str(data).replace('\n', '') + ';;' + wall + ';;' + shelf + ';;' + vol + ';;' + page)
    

    f = open(f'txt/{name}.babel', 'x')
    f.write(content)
    f.close
    

def image():
    
    
    name = input('Name:\n')
    os.system('cls')
    print('Using Clipboard for ID...')
    input('Press Enter to continue')
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    os.system('cls')

    f = open(f'img/{name}.babel', 'x')
    f.write(data)
    f.close





while True:
    os.system('cls')
    print('''

    888b.      8          8 
    8wwwP .d88 88b. .d88b 8 
    8   b 8  8 8  8 8.dP' 8 
    888P' `Y88 88P' `Y88P 8 
                           Generate

        [1] Image
        [2] Text
        [3] Back
        ''')
    imgortxt = input('>> ')
    if imgortxt == '1':
        image()
    elif imgortxt == '2':
        text()
    elif imgortxt == '3':
        break
    else:
        print('Invalid Option')
        input('Press Enter to continue')
        os.system('cls')


