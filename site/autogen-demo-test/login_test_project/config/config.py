import os
################
# Part A
################
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#CHROME_DRIVER_PATH = os.path.join(BASE_DIR, 'resources', 'chromedriver.exe')
#Following is the alternative to ## Part A
#from pathlib import Path
#CHROME_DRIVER_PATH = Path(BASE_DIR) / 'resources' / 'chromedriver.exe'
# Your app URL
#URL = "http://127.0.0.1:5500/site/autogen-demo/index.html"  

## Added post error for the above 
## AttributeError: 'WindowsPath' object has no attribute 'capabilities' 

############################################################
#Part B
############################################################
#from pathlib import Path
#BASE_DIR = Path(__file__).resolve().parent.parent
#CHROME_DRIVER_PATH = Path(BASE_DIR) / 'resources' / 'chromedriver.exe'
#from selenium import webdriver
## Ensure you convert the Path object to a string
#driver = webdriver.Chrome(executable_path=str(CHROME_DRIVER_PATH))
#driver.get("http://127.0.0.1:5500/site/autogen-demo/index.html")


