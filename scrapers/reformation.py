from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import pandas as pd

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# URL of the webpage with dynamic content
url = 'https://www.thereformation.com/tops'

# Navigate to the webpage
items = []
driver.get(url)


#wait for images to load run through the page once
# image_elements = driver.find_elements(By.XPATH, "//img[contains(@class, 'a-image default-image ResolveComplete')]")
driver.find_elements(By.XPATH, '//img[@data-cloudinary-plp-image]')

total_scroll = driver.execute_script("return document.body.scrollHeight")
driver.execute_script("if (window.scrollY > 0) { window.scrollTo(0, 0); }")
step_count = 1
while step_count < 10:
    time.sleep(1)
    scroll_amount = total_scroll*(step_count)/10
    driver.execute_script(f"window.scrollTo({{top: {scroll_amount}, behavior: 'smooth'}});")
    step_count += 1

time.sleep(3)


product_elements = driver.find_elements(By.XPATH, "//a[contains(@class,'product-tile__anchor')]")

for element in product_elements:
    newItem = {}
    try:
        newItem['title']  = driver.find_element(By.XPATH, '//div[@itemprop="name"]').text
        newItem['price'] = driver.find_element(By.XPATH,
                                               '//span[@itemprop="price"]').get_attribute('content')
        newItem['href'] = element.get_attribute('href')
        newItem['color'] = element.find_element(By.CLASS_NAME, "colorName").text

    except:
        # try:
        #     img = element.find_element(By.XPATH, "a-image.ResolveComplete")
        #     newItem['img'] = img.get_attribute("src")
        # except:
            print("will break and not include")

    #iterate through

    img = element.find_element(By.XPATH, "//img[@data-cloudinary-plp-image]")
    newItem['imgs'] = [img.get_attribute("src")]




    items.append(newItem)



# for item in items:
#     link = item['href']
#     driver.get(link)
#     product_description = driver.find_element(By.ID, "product-description")
#     try:
#         field_in_product_description = product_description.find_element(By.TAG_NAME, "p")
#         item['description'] = field_in_product_description.text
#     except:
#         item['description'] = ""


df = pd.DataFrame(items)

driver.quit()

return df
# df = df[df.description != ""]






#
#
#
#
# image_elements = driver.find_elements(By.XPATH, "//img[contains(@class, 'a-image default-image ResolveComplete')]")
# tracker = 0
# while tracker < 2:
#     total_scroll = driver.execute_script("return document.body.scrollHeight")
#     driver.execute_script("if (window.scrollY > 0) { window.scrollTo(0, 0); }")
#     step_count = 1
#     while step_count < 50:
#         time.sleep(1)
#         scroll_amount = total_scroll*(step_count)/50
#         driver.execute_script(f"window.scrollTo({{top: {scroll_amount}, behavior: 'smooth'}});")
#         # driver.execute_script(f"window.scrollTo(0,{scroll_amount});")
#         step_count += 1
#     time.sleep(5)
#
#     image_elements = driver.find_elements(By.XPATH, "//img[contains(@class, 'a-image default-image ResolveComplete')]")
#     tracker += 1
#     print(tracker)
#     print(len(image_elements))
#
# for image in image_elements:
#     print(image.get_attribute('src'))
# print(len(image_elements))


