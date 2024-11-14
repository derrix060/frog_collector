from selenium import webdriver
import pickle

def save_cookies(url, cookies_file):
    driver = webdriver.Chrome()
    driver.get(url)  # Open the website and log in manually

    input("Press Enter after logging in and the page has fully loaded...")

    # Save cookies to a file
    cookies = driver.get_cookies()
    for cookie in cookies:
        print(f"Saving cookie: {cookie}")
    with open(cookies_file, 'wb') as file:
        pickle.dump(cookies, file)

    driver.quit()

if __name__ == "__main__":
    save_cookies("https://zupass.org/#/?folder=frogcrypto", "/Users/mario.apra/Projects/derrix060/frogs/cookies.pkl")