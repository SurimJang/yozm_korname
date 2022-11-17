### Requirements
from selenium import webdriver as wd
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = wd.Chrome(service=Service(ChromeDriverManager().install()))


