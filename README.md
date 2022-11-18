
## Badges

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
![GitHub top language](https://img.shields.io/github/languages/top/SayanInf/Hotel_Management_System)

# Hotel Management System

:hotel: :cityscape: :airplane:

In this era, Hotels are increasing rapidly throughout the whole world. They definitely
need a software which can manage their daily records like Incoming Customer Details, Room distribution, Room Details, 
Bills and Payments etc. Moreover, all of the dataset should be Classified and Private which needs a decent security system.
This Project includes all that. The entire project is open source with MIT License for the contributors and free for distribution. :grinning:









## Features
This project includes...

- Login, Registration System, Logout for the Admins. :closed_lock_with_key:
- Hotel Managagement Main Menu for navigation through different windows . :computer:
- Customers Details Window with flexible Search Bar. :mag:
- Customer Room Distribution Details with Search System. :office:
- Details Tab. :bookmark_tabs:
...and much more. Explore the Software for details.




## Frontend & Backend

- Forntend:  Python
- Backend:  MySQL

## Screenshots

Here are some sneak peeks of the Visuals...

![App Screenshot](https://github.com/SayanInf/Hotel_Management_System/blob/main/Screenshots/Login%20System.png?raw=true)

![App Screenshot](https://github.com/SayanInf/Hotel_Management_System/blob/main/Screenshots/Registration%20Window.png?raw=true)

![App Screenshot](https://github.com/SayanInf/Hotel_Management_System/blob/main/Screenshots/Main%20Menu.png?raw=true)

![App Screenshot](https://github.com/SayanInf/Hotel_Management_System/blob/main/Screenshots/Forgot%20Password.png?raw=true)

![App Screenshot](https://github.com/SayanInf/Hotel_Management_System/blob/main/Screenshots/Customer%20Window.png?raw=true)

![App Screenshot](https://github.com/SayanInf/Hotel_Management_System/blob/main/Screenshots/MySQL%20Details%20get.png)

![App Screenshot](https://github.com/SayanInf/Hotel_Management_System/blob/main/Screenshots/Report%20Window.png?raw=true)

## Prerequisite for Installation

- Basic Programming Knowledge
- Python Programming Knowledge
- MySQL Database Knowledge

- Download the latest version of the python interpreter from [python.org](https://www.python.org/downloads/) and add 'pip' while installation. If you don't have MySQL, download it from [here](https://dev.mysql.com/downloads/installer/) and install it.


## Installation

Follow these set of instructions properly to run the software in your system.

### Step 1: Cloning the Repository
Clone the 'Hotel_Management_System' in any folder of your Windows PC or Download the Zipped Folder of the The Repository manually and Unzip it in any folder of your PC. 
To clone the repository with git bash, run the following codes in the folder you choose to keep the repository.
```bash
  git clone git@github.com:SayanInf/Hotel_Management_System.git
```

### Step 2: Installing required Packages
In the terminal(command prompt/powershell), install 'pillow' library and 'mysql-connector-python' with the following commands...

```bash
  pip install pillow
```
```bash
  pip install mysql-connector-python
```

### Step 3: Database Setup
Open the 'Hotel_Management_System' folder which you downloaded earlier, copy the contents of [MySQLDbcreate.sql](https://github.com/SayanInf/Hotel_Management_System/blob/main/MySQLDBcreate.sql) and paste it in the MySQL command line or Directly open it with MySQL Workbench and click on the lightning icon shown in the top bar. Or, use Command Prompt(cmd) to run the 'MySQLDBcreate.sql' file. Note the MySQL hostname, username, password (andthe name of the schema only if you changed the name) of the given 'hotel_management' Schema.

### Step 4: It's Done! Yaayyy!!!
Run the Hotel Management System.pyw file.

#### Step 5: Optional - It Needs A Bit Coding Experience
If you want to create an .exe file so that you can just click on the icon and it will run the app in any directory like your other programs in windows... :)
We will use pyinstaller package here to convert this 'Hotel_Management_System' python package to .exe file.
use [this version](https://github.com/SayanInf/Hotel_Management_System/tree/optional) of the project. Open all the the python files in the package directory(no need to change the GUIs directory or any secondary directories inclued in the package directory. Only change the primary directory code) and manually edit the image addresses with your folder image addresses to get the image of the package(where I wrote 'change image with your own' in comment line). It is not advisable to do it since, you may miss some address and programme won't run, but still if your are careful with the code you can do it... :) After you are done with it...

First install [pyinstaller package](https://pyinstaller.org/en/stable/operating-mode.html#:~:text=PyInstaller%20reads%20a%20Python%20script,including%20the%20active%20Python%20interpreter!) from pip. 
Again, use terminal and enter
```bash
  pip install pyinstaller
```
if your folder is in another drive first change the drive in command prompt by
```bash
  <Drive Letter>:
```
change the directory to the folder where you saved the 'Hotel_Management_System' package. 
```bash
  cd <the path to the package directory>
```
In the above codes don't include <> in the command.
you can check out [this link](https://www.wikihow.com/Change-Directories-in-Command-Prompt) if you don't know how to change paths using cd command in cmd.
Now, execute the following command...
```bash
  pyinstaller --onefile --windowed icon=logo3.ico Hotel_Management_System.pyw
```
Add an exception if your antivirus is restricting the program from running in the background.

Still if you face issues kindly mention it in the [issues](https://github.com/SayanInf/Hotel_Management_System/issues) section. 

Hope you are successful in installing the package and you are running it without any issue... :grinning:

Wish You A Very Happy Experience With The Software. 

## Developers

- Developer 1: **Sayan Ghosh** 
>Contributions - The Project Lead, The Project Management, The GUI Design, The Registration Window, The Customer System, The Report System, The Logout System, Customer Database, Database Integration, Whole Project Integration, The Dynamic MySQL Details interface, README.md generation, Git Control, GitHub Repository Management, Updates and Upgrades of different features for dynamicity of the Software, Debugging.
- Developer 2: **Purab Jana**
>Contributions - The Main Menu Page, Login System, Registration System, Login & Registration Windows Integration, Login Database, Logout System.
- Developer 3: **Samriddha Karmakar**
>Contributions - The Room System, The Details System, Room Database, Details Database.




## License

[MIT](https://choosealicense.com/licenses/mit/)

(c) MIT License


## Contact Us

>Drop an email on sayanghosh1427@gmail.com
