# Library of Babel saver
Creates .babel/.babelimg files to store text/images. It can also open these files!

# How to use
Just execute babel.py

# Getting information
Visit [The library of babel](https://libraryofbabel.info)

### For images:
1. Visit [this](http://babelia.libraryofbabel.info/imagesearch.html) page and upload your image.
2. Wait for it to finish processing and click on loading
![1](https://i.imgur.com/OdKpCjQ.png)
3. Copy all text in the text box (it's really long)
4. In babel.py under ```Geanerate > Image``` the program will grab the sring directly from your clipboard.

### For text:
1. Visit [this](https://libraryofbabel.info/search.html) page and write some text.
2. Click this:

![2](https://i.imgur.com/wwrcSIF.png)

3. Copy the long string in the text box 
4. IMPORTANT Go back to the page with your text thhere is a chance that the volume value is false!
5. In the image above, at the end of the string you can see ```-wX-sX-vX``` (X standing for a random number) and on the top of the page is the Page number.
6. In babel.py under ```Generate > Text``` Enter your values

# FAQ

### Where are the .babel / .babelimg
They are in /txt or for images in /img 

### Opening images is wired and takes long to load
I have to use selenium for images because you cant call images in the url bar like text. Any suggestions in the issues.


# Credits
[libraryofbabel.info](https://libraryofbabel.info)
