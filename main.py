# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from urllib.request import urlopen, Request
import os
import asyncio
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
import re
import requests
import time


from playwright.async_api import async_playwright

import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
import re
import requests
import time

url = ' https://www.stories.com/en_usd/clothing/tops.html'
driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get(url)
time.sleep(10)
soup = BeautifulSoup(driver.page_source, features="html.parser")
driver.quit()

pics = soup.find_all('picture')
                     # {"class": "a-image.default-image.ResolveComplete"})
for pic in pics:
    print("in here")
    img_url = pic.get('src')
    print(img_url)

# async def main(url):
#
#     driver = webdriver.Chrome()
#     driver.implicitly_wait(30)
#     driver.get(url)
#     soup = BeautifulSoup(driver.page_source, 'lxml')
#     driver.quit()

    # async with async_playwright() as p:
    #     browser = await p.chromium.launch()
    #     page = await browser.new_page()
    #     await page.wait_for_selector('.a-image.default-image')
    #     await page.goto(url)
    #
    #     # Wait for a specific element to appear on the page (you can modify this selector)
    #     await page.wait_for_selector('.a-image.default-image')
    #     # Replace 'img.loaded' with the actual selector for the loaded images
    #
    #     # Select all <img> elements
    #     images = await page.query_selector_all('.a-image.default-image')
    #     # Replace 'img.loaded' with the actual selector
    #     print(len(images))
    #     for image in images:
    #         src = await image.get_attribute('src')
    #         print(src)
    #
    #     await browser.close()
#
# if __name__ == "__main__":
#     url = 'https://www.stories.com/en_usd/clothing/tops.html'
#     main(url)
#     # asyncio.run(main(url))


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     url = 'https://www.stories.com/en_usd/clothing/tops.html'
#     scraper(url)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
