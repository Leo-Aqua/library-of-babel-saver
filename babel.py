import os
import win32clipboard
from win32com.client import Dispatch
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
            os.system('cls')#


def get_chrome_ver():
    def get_version_via_com(filename):
        global crm_version
        parser = Dispatch("Scripting.FileSystemObject")
        try:
            crm_version = parser.GetFileVersion(filename)
        except Exception:
            return None
        return crm_version

    if __name__ == "__main__":
        paths = [r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"]
        crm_version = list(filter(None, [get_version_via_com(p) for p in paths]))[0]
    
    global ncrm_version
    ver = crm_version.startswith('103')
    if ver == True:
        ncrm_version = '103.0.5060.134'
    
    ver = crm_version.startswith('104')
    if ver == True:
        ncrm_version = '104.0.5112.79'
    ver = crm_version.startswith('105')
    if ver == True:
        ncrm_version = '105.0.5195.19'
        



def install():
    # Checks if img and txt directories exist
    isDirimg = os.path.isdir('img')
    isDirtxt = os.path.isdir('txt')
    isFilecrm = os.path.isfile('chromedriver.exe')

    # Creates directories
    print('Installing...')
    if isDirimg == False:
        print('Creating directories...')
        os.mkdir('img')
        f = open('img/.babelimg', 'w')
        f.write('PLACEHOLDER')
        f.close
        print('Done!')
    if isDirtxt == False:
        print('Creating directories...')
        os.mkdir('txt')
        f = open('txt/.babel', 'w')
        f.write('PLACEHOLDER')
        f.close
        print('Done!')
    if isFilecrm == False:
        print('Downloading chromedriver...')
        # downloads choromedriver
        import requests
        from zipfile import ZipFile
        print('Chrome version: ' + ncrm_version)
        url = f'https://chromedriver.storage.googleapis.com/{ncrm_version}/chromedriver_win32.zip'
        response = requests.get(url)
        open("driver.zip", "wb").write(response.content)
        print('Zip downloaded!')
        print('Extracting...')
        zf = ZipFile('driver.zip', 'r')
        zf.extractall('.')
        zf.close()
        print('Done!')
        print('removing zip...')
        os.remove('driver.zip')
    print('Done!')


get_chrome_ver()
install()
main()
