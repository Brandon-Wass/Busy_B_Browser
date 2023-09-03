# Busy_B_Browser

Welcome to the Busy B Browser!

This is a simple web browser that is still in the works.

As of right now, the browser is in the early stages of development, but it still functions as a single page browser with download capability and basic function buttons.


I built this because I got tired of using Chrome, Edge, and other browsers that always seem to track your information. This browser does not save any user data whatsoever upon closing! That's right! Every time you open the browser, you will start with a fresh slate. No saving passwords, addresses, payment information, cookies, or even browsing history!

I will be working on implementing a few other functions into the app over time. Functions such as: tabbed browsing, bookmarks, .pdf .xml. html and other formats of file viewing.

Star and watch this repo to keep up with updates and new versions along the way, and do away with all those clunky browsers that like to send your information all over the place!

Should you decide to clone this repo, make sure to keep the .py file and .ico file together, as the script calls for the .ico file. Otherwise, your system will fail to run the script.

If you are on a windows system, compile this program into an executable file for easy browsing and to replace your daily browser using the following command:
pyinstaller -w -F -i .\busyb.ico .\private_browser.py

To run this program as a python script, you will need to install the dependencies needed first using:
pip install pyqt5 pyqtwebengine

If you've compiled this program into an .exe file on a windows system, you will find the .exe file in the newly created dist folder in the directory you have the .py and .ico files saved to. To run the compiled file, simply open the .exe file.
To run as a python script on windows without depending on the terminal staying open, open a terminal in the directory containing the .py file and use:
pythonw .\private_browser.py

On Linux based systems, open a terminal in the directory containing the .py file and use:
DISPLAY=:0 nohup python3 $(find / -name "case_fan_tach.py" 2>/dev/null) >/dev/null 2>&1 &

Thanks for trying out this simple web browser, and I hope you enjoy!
