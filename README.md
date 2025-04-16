# Introduction
This is a simple automated testing of a open-source website designed for allowing other programmers such as myself to test QA automation using Selenium and Pytest. The website can be found here: 

https://opensource-demo.orangehrmlive.com/
# Pre-requisites
- Windows Subsystem for Linux 2
- Windows 11
- VSCode
- VSCode WSL Remote Extension

Could probably work on any Linux Distro.

# First time WSL Set-up
```
wsl install
``` 
# Install Latest Ubuntu
```
wsl --install ubuntu
```
# Get Ubuntu Updates
```
sudo apt update
```
# Get Full Python
```
sudo apt install python3-full
```
# Get pip
```
sudo apt install python3-pip
```
# Create Virtual Environment
```
python3 -m venv qa_automate
```
# Get Chrome Driver for Selenium and Pytest
```
sudo apt install chromium-chromedriver
```

# Get Packages for Environment
Note: `sudo` and `--break-system-packages` are crucial to allow pip packages to be installed inside the environment. Otherwise it defaults to installing GLOBALLY.

```
source qa_automate/Scripts/activate \
sudo pip install selenium pytest --break-system-packages

```
# To Run Automation Tests
Note: cmd should be run in this folder where this README is.
```
pytest -v
```
# Additional Notes
To use pytest, you test python scripts MUST have `test_` in front of them, for eg. `test_login.py`.

# Future Improvements
1. A way to automate set-up. 
2. Debug Virtual Environments on Ubuntu in WSL and find out why it keeps throwing error about externally managed environments.
3. More Tests