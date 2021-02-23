import requests
from secrets import API_KEY

def get_group_id(group_url):
    # https://www.flickr.com/services/api/flickr.urls.lookupGroup.html

    url = f'https://www.flickr.com/services/rest/?method=flickr.urls.lookupGroup&api_key={API_KEY}&url={group_url}&format=json&nojsoncallback=1'

    r = requests.get(url).json()
    group_id = (r['group']['id'])

    return group_id

def get_photo_ids(group_id):
    # https://www.flickr.com/services/api/flickr.photos.search.html

    url = f'https://www.flickr.com/services/rest/?method=flickr.photos.search&api_key={API_KEY}&group_id={group_id}&format=json&nojsoncallback=1&page=1&per_page=10'

    r = requests.get(url).json()

    # Flickr paginates the resuts. Default is 100 results per page, max is 500.
    total_pages = r['photos']['pages']

    photo_ids = []
    for photo in r['photos']['photo']:
        photo_ids.append(photo['id'])

    return photo_ids

def get_photo_urls(photo_ids):
    # https://www.flickr.com/services/api/flickr.photos.getSizes.htm
    
    photo_urls = []
    for photo_id in photo_ids:
        url = f'https://www.flickr.com/services/rest/?method=flickr.photos.getSizes&api_key={API_KEY}&photo_id={photo_id}&format=json&nojsoncallback=1'

        r = requests.get(url).json()
        photo_urls.append(r['sizes']['size'][0]['source'])
    
    return photo_urls

group_url = 'https://www.flickr.com/groups/velvia50/pool/'

print('STEP 1/4: Finding group\n-')
group_id = get_group_id(group_url)

print('STEP 2/4: Getting photo IDs\n-')
photo_ids = get_photo_ids(group_id)

print('STEP 3/4: Converting IDs to URLs\n-')
photo_urls = get_photo_urls(photo_ids)

print('STEP 4/4: Downloading photos\n-')