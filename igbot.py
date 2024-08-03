from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from password import pw
from random import randint

class Bot():
    links = []

    comments = [
        'AMAZING SHOT', 'Love it!'
    ]

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.login('wet_wick', pw)
        self.like_comment_by_hashtag('travel photos')

    def login(self, username, password):
        self.driver.get('https://instagram.com/')
        wait = WebDriverWait(self.driver, 30)

        try:
            username_input = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')))
            username_input.send_keys(username)

            password_input = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
            password_input.send_keys(password)

            login_button = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
            login_button.click()

            # Handle "Not Now" prompts
            not_now_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]")))
            not_now_button.click()

            not_now_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]")))
            not_now_button.click()
        except Exception as e:
            print(f"Error during login: {e}")

    def like_comment_by_hashtag(self, hashtag):
        self.driver.get(f'https://www.instagram.com/explore/tags/{hashtag}/')
        wait = WebDriverWait(self.driver, 30)
        sleep(5)  # Allow time for the page to load

        print("Finding links to posts...")
        links = self.driver.find_elements(By.TAG_NAME, 'a')

        def condition(link):
            return '.com/p/' in link.get_attribute('href')

        valid_links = list(filter(condition, links))

        print(f"Found {len(valid_links)} valid post links.")
        for i in range(min(5, len(valid_links))):
            link = valid_links[i].get_attribute('href')
            if link not in self.links:
                self.links.append(link)

        # Like and comment on posts
        for link in self.links:
            self.driver.get(link)
            sleep(3)  # Allow time for the page to load

            try:
                print(f"Interacting with post: {link}")

                # Updated XPath for like button
                like_button_xpath = '//span[@aria-label="Like"]'
                print(f"Trying to find like button with XPath: {like_button_xpath}")
                like_button = wait.until(EC.element_to_be_clickable((By.XPATH, like_button_xpath)))
                like_button.click()
                print(f"Post liked successfully")
                sleep(5)  # Wait to ensure the like action is processed

                # Click on comment area to open comment box
                comment_area_xpath = "/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/div/textarea"
                print(f"Trying to find comment area with XPath: {comment_area_xpath}")
                comment_area = wait.until(EC.presence_of_element_located((By.XPATH, comment_area_xpath)))
                comment_area.click()
                sleep(1)

                # Find the comment box
                comment_box_xpath = "/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/div/textarea"
                print(f"Trying to find comment box with XPath: {comment_box_xpath}")
                comment_box = wait.until(EC.presence_of_element_located((By.XPATH, comment_box_xpath)))
                comment_box.send_keys(self.comments[randint(0, 1)])
                sleep(1)

                # Submit the comment
                submit_button_xpath = "/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/div/div[2]/div"
                print(f"Trying to find submit button with XPath: {submit_button_xpath}")
                submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, submit_button_xpath)))
                submit_button.click()
                print(f"Comment posted successfully on {link}")
            except Exception as e:
                print(f"Error interacting with post {link}: {e}")

def main():
    while True:
        my_bot = Bot()
        sleep(30 * 60)  # Sleep for 30 minutes

if __name__ == '__main__':
    main()
