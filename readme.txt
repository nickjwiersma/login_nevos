Made using Python3.11 and any newer versions should work.
Keeping in mind you have basic Python language knowledge and know how to use it on your own OS.


Install the Python required packages using:
pip install -r requirements.txt
pip install geckodriver-autoinstaller


Since most people prefer chrome this script is initially set to use Chrome as the webdriver.
However if you wish to use Firefox apply these changes:
Remove the # at the beginning of line: 8, 9 and 19
Add a # at the beginning of line: 4, 5 and 16


Edit the code on line 22 within the quotation marks to the email address you use to log in:
un = "your_login_credentials"

Edit the code on line 23 within the quotation marks to the password you use to log in:
pw = "your_password"


Save script and run using Python3.11


Enjoy!
