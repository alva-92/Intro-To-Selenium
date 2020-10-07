from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

"""
    Initializing the driver and running a basic search

    For this we will use Google as an endpoint
"""
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('http://google.com')
element = driver.find_element_by_name('q') # Return the search element
element.send_keys('Intro to Selenium')
element.send_keys(Keys.RETURN)             # Simulate enter

"""
    Finding an element by its xPath

    For this we will use the Selenium HQ page. We need to idenfity
    a unique element. In this case we will copy the xPath of the
    element in order to get a unique identifier. This is done
    by inspecting the element, right clicking on copy and selecting 
    copy xPath.

    Note the xPath and IDs could change without notice. Verify 
    they are up to date
"""
driver.get('https://www.selenium.dev/')
element = driver.find_element_by_xpath('//*[@id="header"]/a[1]/img[1]')
element.click()

"""
    Finding an element by its id and navigating to 
    another page

    For this we will use the Selenium HQ page. 
"""
driver.get('https://www.selenium.dev/')
element = driver.find_element_by_id('gsc-i-id1')
element.send_keys('webdriver')
element.send_keys(Keys.RETURN) 
#btn = driver.find_element_by_id('___gcse_0')
#btn.click()
time.sleep(3)
driver.switch_to.frame('master-1')

"""
    Sorting through specific elements and retrieving data

    For this we will use the Php travels site. 
"""
driver.get('https://phptravels.net/offers')
price_tags = driver.find_elements_by_css_selector('.price span') # Find the price class and get the actual price within the span
price_list = []
for p in price_tags:
    price_list.append(p.text)

print(price_list)

clean_price_list = []

for price in price_list:
    if price.startswith('$'):
        price_num = price[1:] # remove the first character $
        price_val = int(price_num.replace(',', ''))
        clean_price_list.append(price_val)

print(clean_price_list)
