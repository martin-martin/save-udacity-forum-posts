# remove the last number (reply identifier) to have clean link URLs to
# every thread. for aiming to scrape the whole thread.
# NOTE: see README.md for issues and pointers in regards to that
import re
import json

with open('raw_links.json', 'r') as f:
    all_links = json.load(f)

# identify whether there is a final URL section with a reply number
pattern = re.compile(r'(\/\d{1,3})$')

# cutting off the final part, if there is one
base_links = []
for link in all_links:
    if re.search(pattern, link):
        base_link = '/'.join(link.split('/')[:-1])
        base_links.append(base_link)
    else:
        base_links.append(link)

links = set(base_links)  # removing duplicates
print(len(base_links), len(links))

# in order to write to a JSON file we need a list (or dict)
llinks = list(links)
with open('links.json', 'w') as f:
    json.dump(llinks, f)
