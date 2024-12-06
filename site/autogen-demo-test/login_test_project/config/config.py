import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#Part A
#CHROME_DRIVER_PATH = os.path.join(BASE_DIR, 'resources', 'chromedriver.exe')

#Following is the alternative to ## Part A
from pathlib import Path
CHROME_DRIVER_PATH = Path(BASE_DIR) / 'resources' / 'chromedriver.exe'

# Your app URL
URL = "http://127.0.0.1:5500/site/autogen-demo/index.html"  