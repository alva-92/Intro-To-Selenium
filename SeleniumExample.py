from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


"""
    Initializing the driver and running a basic search

    For this we will use Google as an endpoint
"""
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('http://google.com')
element = driver.find_element_by_name('q') # Return the search element
element.send_keys('Intro to Selenium')
element.send_keys(Keys.RETURN)             # Simulate enter

