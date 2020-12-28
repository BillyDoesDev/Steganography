# Steganography
A small python script that allows you to hide secret messages inside images and vice-versa 
 
```
888b.           8    8    8  dP       w      8      w     d8 8888 .d88b. 
8   8 .d88 8d8b 8.dP 8.dP 8wdP  8d8b. w .d88 8d8b. w8ww  dP8 8ww. 8P  Y8 
8   8 8  8 8P   88b  88b  88Yb  8P Y8 8 8  8 8P Y8  8   dPw8   `8 8b  d8 
888P' `Y88 8    8 Yb 8 Yb 8  Yb 8   8 8 `Y88 8   8  Y8P    8 Y88P `Y88P' 
                                        wwdP                             
```
 
## Requires Python3
 
## Note(for Linux users):
 
Some Linux distros may not have pip installed by default. In that case, you may need to install it manually on your system.
Users running a Debian based OS such as Ubuntu may install it by `sudo apt install python3-pip`</br>
Additionally, the `pyperclip` module which has been used in this project depends on the OS to access the clipboard contents.
Some Linux distros may not have certain packages to do so by default. Ubuntu, for example, lacks the required packages.
Users running a Debian based OS such as Ubuntu may install the required package by `sudo apt install xclip`
 
Read the official `pip` and `pyperclip` documentation for more info...
 
## Recommended: Create a virtual python environment to house the dependencies of this project
 
Clone/extract this project into the required directory and then, fire up a terminal (or `CMD` in case of Windows) there and then create a python virtual environment there
 
**Windows:**
`python -m venv venv`
 
**Linux:**
`python3 -m venv venv`
 
Once the virtual environment has been created, activate it
 
**Windows:**
`venv\Scripts\activate.bat`
 
**Linux:**
`source venv/bin/activate`
 
*You should see `(venv)` appear before your prompt in the terminal, indicating that the virtual environment has been activated...*
Then install the project requirements(The modules used are specified in the `requirements.txt` file)
 
**Windows/Linux:**`pip install -r requirements.txt`
 
Once the requirements have been satisfied, the script is ready to run...
 
**Windows/Linux:**`python script.py`
 
If you want to re-run the script, simply activate the virtual environment again and then run it by `python script.py`
There is also a sample png image which has been included by the name of `sample.png`. You may use it for testing...
 
## Limitations:
 
1. This script is CPU intensive
2. Works best on PNGs
3. The resulting PNG image loses its transparency (if any)
4. Some Unicode characters cannot be read properly... Using uncommon characters may break the code (all punctuations work fine though)
5. The max number of characters that can be encoded in an image depends upon its resolution... For example, an image of resolution 1920 by 1080 pixels can accommodate `(1920*1080)/3 = 691200` characters only.
</br></br>
 
**ENJOY!!**
 
If you copy or distribute any part of this project, then be sure to give @DarkKnight450 credits and show some love...</br>
Feel free to contact me at DarkKnight450@protonmail.com
Any feedback/suggestions would be highly valued... 
 
</> with ♡, on GitHub
 


