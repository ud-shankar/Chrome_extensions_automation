from selenium import webdriver
from selenium.webdriver.chrome.options import Options


chromedriver = 'C:/Selenium/chromedriver.exe'               #path where your local chrome driver is saved
chrome_options = Options()
chrome_options.add_argument("start-maximized")
chrome_options.add_extension(r"C:\Oslash\Drivers\dictionary.crx")       #path to your .crx file in your local
driver = webdriver.Chrome(executable_path=chromedriver, options=chrome_options)
