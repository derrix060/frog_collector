from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle
import time

def load_cookies(driver, cookies_file):
    with open(cookies_file, 'rb') as file:
        cookies = pickle.load(file)
        for cookie in cookies:
            print(f"Adding cookie: {cookie}")
            driver.add_cookie(cookie)

def test_frog_requests():
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.get("https://zupass.org/#/?folder=frogcrypto")  # Open a page to set cookies

    modal_path = "body > div.ReactModalPortal > div > div > div > div"
    input("Press Enter when you added your credentials...")

    with open('urls', 'r') as file:
        urls = file.readlines()

    size = len(urls)
    for idx, url in enumerate(urls):
        # if idx < 1000:
        #     continue
        url = url.strip()
        print(f"Processing URL {idx + 1}/{size}: {url}")
        driver.get(url)
        try:
            # Wait for the "send FROG REQUEST" button to appear and click it
            iframe = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "iframe"))
            )
            driver.switch_to.frame(iframe)

            # Click on all requests
            clicked_on_send = False
            count = 0
            while clicked_on_send is False and count < 30:
                count += 1
                spam = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, f"{modal_path} > div > span.text-rarity-rare.text-center.uppercase.font-bold.text-xl"))
                )
                if "(+1" not in spam.text:
                    print("Already connected, skipping...")
                    clicked_on_send = True
                    continue
                while clicked_on_send is False:
                    element = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, f"{modal_path} > button.w-48.text-sm.bg-green-500.text-white.px-4.py-2.rounded-sm.flex-1"))
                    )
                    try:
                        element.click()
                    except Exception:
                        continue
                    if element.text.startswith("send"):
                        clicked_on_send = True
                    print(f"Clicked on button: {element.text}")
                    time.sleep(0.5)
        except Exception:
            pass

    driver.quit()

if __name__ == "__main__":
    test_frog_requests()
