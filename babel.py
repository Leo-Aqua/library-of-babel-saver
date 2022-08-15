import os
import win32clipboard

def gen():
    

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

        f = open(f'img/{name}.babelimg', 'x')
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
            main()
        else:
            print('Invalid Option')
            input('Press Enter to continue')
            os.system('cls')


def read():
    import os
    from time import sleep





    def text():
        while True:
            try:
                os.system('cls')
                print('Avalible files:\n')
                dir = str(os.listdir("txt")).replace('[', '').replace(']', '').replace('.babel', '').replace("'", '').replace(',', '\n')
                print(dir)
                file = input('\nFile: ')
                f = open('txt/'+file+'.babel', 'r')
                break
            except FileNotFoundError:
                os.system('cls')
                print('file not found!')
        a = f.read()
        f.close
        dict = a.split(';;')
        
        os.system(f'start https://libraryofbabel.info/book.cgi?{dict[0]}-w{dict[1]}-s{dict[2]}-v{dict[3]}:{dict[4]}')

    def image():
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.webdriver.common.keys import Keys
        import win32clipboard
        while True:
            try:
                os.system('cls')

                print('Avalible files:\n') #list files
                dir = str(os.listdir("img")).replace('[', '').replace(']', '').replace('.babelimg', '').replace("'", '').replace(',', '\n')
                print(dir)
        
                file = input('\nFile: ')
                f = open('img/'+file+'.babelimg', 'r')
                break
            except FileNotFoundError:
                os.system('cls')
                print('file not found!')
        a = f.read()
        f.close

        driver = webdriver.Chrome()
        driver.get("https://babelia.libraryofbabel.info/slideshow.html")
        sleep(3)
        elem = driver.find_element(By.ID, "loc")
        elem.click()
        sleep(1)
        textarea = driver.find_element(By.ID, "values")
        textarea.click()
        textarea.send_keys(Keys.CONTROL + 'a')

        

        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardText(a)
        win32clipboard.CloseClipboard()

        textarea.send_keys(Keys.CONTROL + 'v')
        sleep(1)
        textarea.send_keys(Keys.ENTER)
        while True:
            try:
                _ = driver.window_handles
            except:
                break
            sleep(1)
        
    while True:
        os.system('cls')
        print('''

        888b.      8          8 
        8wwwP .d88 88b. .d88b 8 
        8   b 8  8 8  8 8.dP' 8 
        888P' `Y88 88P' `Y88P 8 
                            Read
                            
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
            main()
        else:
            print('Invalid Option')
            input('Press Enter to continue')
            os.system('cls')


def main():
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
            gen()
            
        elif choice == '2':
            read()
           
            
        elif choice == '3':
            quit()
        else:
            print('Invalid Option')
            input('Press Enter to continue')
            os.system('cls')
main()
