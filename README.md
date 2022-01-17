#### A bullshit application

_A do nothing python gui app for reference._


---
- Development Platform
    - Ubuntu 21.10
- IDE
    - Visual Studio Code v1.63.2
- Python3
    - v3.9.7
- External Dependencies
    - sty
---
### _Working out code in a virtual environment_
- *Install virtualenv*
    - sudo apt install virtualenv -y
- *Initialize project directory*
    - virtualenv -p /path/to/python Or "$(which python3)" project-name
- *Change into the project directory*
- *Activate the environment*
    - source bin/activate
- *Install environment dependencies*
    - pip3 install sty lxml
- *To deactivate the environment*
    - deactivate
### _Script Usage_
- *Install external libraries*
    - pip3 install sty lxml
- *Add script location to PATH*
    - I added if statement to ~/.profile
- *Refresh environment*
    - source ~/.profile