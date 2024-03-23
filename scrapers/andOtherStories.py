import time
import pandas as pd
import json
from concurrent.futures import ThreadPoolExecutor
from selenium.webdriver.common.by import By


from selenium import webdriver

# PROXY = "162.246.248.214:80"
# PROXY = "144.126.141.115:1010"

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--proxy-server=%s' % PROXY)
chrome_options.add_argument("--headless=new")

driver = webdriver.Chrome(options=chrome_options)

#test new proxy
# driver.get("http://httpbin.org/ip")
# print(driver.find_element(By.TAG_NAME, "body").text)


url = 'https://www.stories.com/en_usd/clothing/tops.html'


def process_item(item):
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--proxy-server=%s' % PROXY)
    chrome_options.add_argument("--headless=new")

    driver = webdriver.Chrome(options=chrome_options)
    try:
        link = item['href']
        driver.get(link)
        product_schema = driver.find_element(By.ID, "product-schema").get_attribute('innerHTML')
        product_schema_json = json.loads(product_schema)
        item['imgs'] = product_schema_json.get('image')
        item['description'] = product_schema_json.get('description')
    except:
            # for if the product-schema isn't available
            # try:
            #     product_description = driver.find_element(By.ID, "product-description")
            #     field_in_product_description = product_description.find_element(By.TAG_NAME, "p")
            #     item['description'] = field_in_product_description.text
            #     item['color'] = driver.find_element(By.ID, "swatchDropdown").get_attribute("data-value")
            # except:
        item['description'] = ""
        item['imgs'] = ""


def scrape_data():
    # Navigate to the webpage
    driver.get(url)
    items = []

    #scrolls through page
    driver.find_elements(By.XPATH, "//img[contains(@class, 'a-image default-image ResolveComplete')]")
    total_scroll = driver.execute_script("return document.body.scrollHeight")
    driver.execute_script("if (window.scrollY > 0) { window.scrollTo(0, 0); }")
    step_count = 1
    total_steps = 5
    while step_count < total_steps:
        scroll_amount = total_scroll*(step_count)/total_steps
        driver.execute_script(f"window.scrollTo({{top: {scroll_amount}, behavior: 'smooth'}});")
        step_count += 1

    time.sleep(.5)

    #grabs all elements on the page
    product_elements = driver.find_elements(By.XPATH, "//div[contains(@class,'o-product producttile-wrapper')]")

    print("LENGTH OF PRODUCT ELEMENTS :" + str(len(product_elements)))
    for element in product_elements:
        newItem = {}
        try:
            # description = element.find_element(By.CLASS_NAME, "description")
            newItem['title'] = element.find_element(By.CLASS_NAME, "productName").get_attribute('textContent')
            newItem['price'] = element.find_element(By.CLASS_NAME, "price").get_attribute('textContent')
            newItem['href'] = element.find_element(By.TAG_NAME, "a").get_attribute('href')
            newItem['color'] = element.find_element(By.CLASS_NAME, "colorName").get_attribute('textContent')
            items.append(newItem)
        except:
            print("will break and not include")

    # goes to each link
    #run in headless mode

    print("LENGTH OF ITEMS: " + str(len(items)))

    # # Assuming 'items' is a list of links
    with ThreadPoolExecutor() as executor:
        executor.map(process_item, items[:12])


    driver.quit()


    df = pd.DataFrame(items)

    if df.empty:
        print("ERROR, must log")
        return None

    df = df[df['description'] != ""]
    company_name = 'and other stories'
    df['company_name'] = company_name
    df["base_url"] = "https://www.stories.com/"

    print("Return DF:")
    print(df)


    return df

    # print(df.to_string())
    # print(len(df))

    # compression_opts = dict(method='zip',
    #                         archive_name='otherStories.csv')
    # # df.to_csv('otherStories.zip', index=False,
    # #           compression=compression_opts)
    #
    #
    # #now you have a pandas datafrmae



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

if __name__ == "__main__":
    scrape_data()
