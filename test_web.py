from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdrivermanager.chrome import ChromeDriverManager
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


class TestDefaultSuite():
    def setup_method(self, method):
        chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
        chrome_options = Options()
        options = [
            "--headless",
            "--disable-gpu",
            "--window-size=1920,1200",
            "--ignore-certificate-errors",
            "--disable-extensions",
            "--no-sandbox",
            "--disable-dev-shm-usage"
        ]
        for option in options:
            chrome_options.add_argument(option)

        self.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    def teardown_method(self, method):
        self.driver.quit()

    def test_login(self):
        self.driver.get("http://localhost:8080/dev/chose.xhtml")
        self.driver.find_element(By.NAME, "j_idt89:j_idt97").click()
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".success > td:nth-child(1)")
        assert len(elements) > 0
