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
    from selenium.webdriver.chrome.options import Options


    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    while True:
        try:
            os.system('cls')

            print('Avalible files:\n') #list files
            dir = str(os.listdir("img")).replace('[', '').replace(']', '').replace('.babel', '').replace("'", '').replace(',', '\n')
            print(dir)
    
            file = input('\nFile: ')
            f = open('img/'+file+'.babel', 'r')
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
        break
    else:
        print('Invalid Option')
        input('Press Enter to continue')
        os.system('cls')