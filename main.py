import os
import datetime
import requests
import urllib.request as req
from tqdm import tqdm

import settings
from secrets import API_KEY

def get_group_id(group_url):
    # https://www.flickr.com/services/api/flickr.urls.lookupGroup.html

    url = f'https://www.flickr.com/services/rest/?method=flickr.urls.lookupGroup&api_key={API_KEY}&url={group_url}&format=json&nojsoncallback=1'

    r = requests.get(url).json()
    group_id = (r['group']['id'])

    return group_id

def get_photo_ids(group_id, n=0, page=1, photo_ids=[]):
    # https://www.flickr.com/services/api/flickr.photos.search.html

    # determine the number of imgs to display per page
    # max is 500, then the api paginates
    if settings.NUMBER_OF_IMGS < 500:
        per_page = settings.NUMBER_OF_IMGS
    else:
        per_page = 500

    url = f'https://www.flickr.com/services/rest/?method=flickr.photos.search&api_key={API_KEY}&group_id={group_id}&format=json&nojsoncallback=1&page=1&per_page={per_page}&page={page}'
   
    r = requests.get(url).json()

    for photo in r['photos']['photo']:
        if n < settings.NUMBER_OF_IMGS:
            photo_ids.append(photo['id'])
            n += 1

    total_pages = r['photos']['pages']

    if (n < settings.NUMBER_OF_IMGS) and (page < total_pages):
        # if we've gotten all the imgs on a page, 
        # and we still need more imgs to hit the quota,
        # go to next page (assuming there is one) 
        page += 1
        get_photo_ids(group_id, n, page, photo_ids)

    return photo_ids

def get_photo_urls(photo_ids):
    # https://www.flickr.com/services/api/flickr.photos.getSizes.htm
    
    photo_urls = []
    for photo_id in tqdm(photo_ids):
        url = f'https://www.flickr.com/services/rest/?method=flickr.photos.getSizes&api_key={API_KEY}&photo_id={photo_id}&format=json&nojsoncallback=1'

        r = requests.get(url).json()
        photo_urls.append(r['sizes']['size'][settings.SIZE]['source'])
    
    return photo_urls


#group_url = 'https://www.flickr.com/groups/velvia50/pool/'
print('Welcome to flickGroups-dl')
print('Enter a flickr group URL:')
group_url = input('')

print('\n🌘 STEP 1/4: Finding group')
group_id = get_group_id(group_url)

print('\n🌗 STEP 2/4: Getting photo IDs')
photo_ids = get_photo_ids(group_id)

print('\n🌖 STEP 3/4: Converting IDs to URLs\n')
photo_urls = get_photo_urls(photo_ids)

print('\n🌕 STEP 4/4: Downloading photos\n')
# see if "downloads" folder exists 
downloads_dir_exists = os.path.isdir('downloads')
if downloads_dir_exists:
    pass
else:
    os.mkdir('downloads')

# create a folder using datetime
current_date = datetime.datetime.now().strftime('%Y-%m-%d_%H%M%S')
os.mkdir(f'downloads/{current_date}')

# write urls to txt file
with open(f'downloads/{current_date}/urls.txt', 'w') as f:
    for url in photo_urls:
        f.write("%s\n" % url)

# download jpgs from url
for url in tqdm(photo_urls):
    name = url.split('.com/')[1].split('/')[1].split('.')[0]
    req.urlretrieve(url, f'downloads/{current_date}/{name}.jpg')

print('\n✅ Done')