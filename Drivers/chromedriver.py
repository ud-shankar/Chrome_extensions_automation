from selenium import webdriver

chromedriver = 'C:/Selenium/chromedriver.exe'               #path where your local chrome driver is saved
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_extension("../Source/dictionary.crx")
driver = webdriver.Chrome(chromedriver, options=options)

