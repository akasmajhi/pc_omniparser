import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHROME_DRIVER_PATH = os.path.join(BASE_DIR, 'resources', 'chromedriver.exe')
URL = "http://127.0.0.1:5500/site/autogen-demo/index.html"  # Your app URL