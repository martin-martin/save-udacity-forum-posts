import os
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
# ------------------------------------------------------------ #

driver = webdriver.Chrome(chromedriver_local_path)
driver.get(forum_user_activity_url)

# quick sign-in
email_path = '//*[@id="app"]/div/div[2]/div/div/div/div[2]/div/div[1]/div/form/div/div[1]/input'
email_elem = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, email_path)))
email_elem.send_keys(email + Keys.TAB + password + Keys.ENTER)
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, 'user-right')))

# get personal posts and some of the surrounding ones
# NOTE: if you want complete threads, also if the thread is really long
#       see the note in README.md
with open('raw_links.json', 'r') as f:
    links = json.load(f)
links = set(links) # remove duplicates

for link in links:
    driver.get(link)
    # wait a moment, maybe something needs loading
    time.sleep(3)
    # fetching the name of the post, check 'test.py' for more info
    if len(link.split('/')) == 7:
        name = link.split('/')[-3]
    else:
        name = link.split('/')[-2]
    # NOTE: naming will result in overwriting previous same-name files
    #       this could be a problem if you posted twice in a thread with
    #       a lot of other people's posts in between!
    #
    # get the source code and write it to file
    html = driver.page_source
    with open(f'my_posts/{name}.html', 'w') as f:
        f.write(html)
