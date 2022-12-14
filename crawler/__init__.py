from selenium import webdriver as wd
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class DynamicRequest(object):
    chrome_options = wd.ChromeOptions()

    def __init__(self, options=None):
        self.service = Service(ChromeDriverManager().install()) 
        self.options = ['--headless', '--disable-gpu', 'window-size=1920x1080']
        self._set_option(options)
        self.driver = wd.Chrome(service=self.service, options=self.chrome_options)

    def _set_option(self, options):
        if options is not None:
            self.options += options

        self.chrome_options = wd.ChromeOptions()
        for opt in set(self.options):
            self.chrome_options.add_argument(opt)

    def get(self, url, callback=None):
        self.driver.get(url)
        return callback(response=self.driver)
