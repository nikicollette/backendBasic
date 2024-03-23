from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# URL of the webpage with dynamic content
url = 'https://www.stories.com/en_usd/clothing/tops.html'

# Navigate to the webpage
driver.get(url)

# Scroll and interact with the page to trigger the loading of images
while True:
    print("entered")
    # Get the current number of loaded images
    driver.execute_script("if (window.scrollY > 0) { window.scrollTo(0, 0); }")

    image_elements = driver.find_elements(By.XPATH, "//img[contains(@class, 'a-image ResolveComplete')]")
    current_image_count = len(image_elements)
    print(current_image_count)
    driver.execute_script("window.scrollTo({top: document.body.scrollHeight, behavior: 'smooth'});")


    # Wait briefly for new images to load (adjust the sleep time as needed)
    time.sleep(5)

    # Get the new number of loaded images after scrolling
    try:
    image_elements = driver.find_elements(By.XPATH, "//img[contains(@class, 'a-image ResolveComplete')]")
    new_image_count = len(image_elements)

    # If no new images were loaded, break out of the loop
    if new_image_count == current_image_count:
        break

# Find and extract all image URLs
image_elements = driver.find_elements(By.XPATH, "//img[contains(@class, 'a-image ResolveComplete')]")
image_urls = [img.get_attribute('src') for img in image_elements]

# Print the image URLs
for image in image_urls:
    print(image)
# Close the WebDriver when you're done

print(len(image_urls))
driver.quit()
