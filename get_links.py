import os
import re
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


# ------------------------------------------------------------ #
# ------------- INDIVIDUAL SET-UP (CHANGE THIS!) ------------- #
# ------------------------------------------------------------ #
chromedriver_local_path = '/Users/martin/Documents/projects/posts/chromedriver'
forum_user_activity_url = 'https://discussions.udacity.com/u/martin-martin/activity'
# if you don't use virtualenvs and environment vars, replace this
# with your email and pwd as a string (but don't commit to GitHub!!)
email = os.environ.get('UDACITY_EMAIL')  # or replace with string
password = os.environ.get('UDACITY_PWD')  # or replace with string
# depends on how many posts you have made
# (= how often do you have to scroll on your activity page in
# order to load all the posts)
num_scrolls = 100
# ------------------------------------------------------------ #

driver = webdriver.Chrome(chromedriver_local_path)
driver.get(forum_user_activity_url)

# quick sign-in
email_path = '//*[@id="app"]/div/div[2]/div/div/div/div[2]/div/div[1]/div/form/div/div[1]/input'
email_elem = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, email_path)))
email_elem.send_keys(email + Keys.TAB + password + Keys.ENTER)
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, 'user-right')))

# scroll to fetch all posts
body_elem = driver.find_element_by_css_selector('body')
for _ in range(num_scrolls):  # scroll to the bottom to load all posts
    body_elem.send_keys(Keys.PAGE_DOWN + Keys.PAGE_DOWN)
    time.sleep(0.5)

# now let's get all links we want (and only those)
pattern = re.compile(r'^(https:\/\/discussions\.udacity\.com\/t\/)')
link_list = []
elems = driver.find_elements_by_xpath("//a[@href]")
for elem in elems:
    url = elem.get_attribute("href")
    if re.match(pattern, url):
        link_list.append(url)

# save to file to inspect and work forward with
with open('raw_links.json', 'w') as f:
    json.dump(link_list, f)
