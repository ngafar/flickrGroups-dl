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

    url = f'https://www.flickr.com/services/rest/?method=flickr.photos.search&api_key={API_KEY}&group_id={group_id}&format=json&nojsoncallback=1&page=1&per_page=500'

    r = requests.get(url).json()

    # Flickr paginates the resuts. Default is 100 results per page, max is 500.
    total_pages = r['photos']['pages']

    pic_ids = []
    for pic in r['photos']['photo']:
        pic_ids.append(pic['id'])

    return pic_ids

def get_photo_urls(photo_ids):
    # https://www.flickr.com/services/api/flickr.photos.getSizes.htm

    for photo_id in photo_ids:
        url = f'https://www.flickr.com/services/rest/?method=flickr.photos.getSizes&api_key={API_KEY}&photo_id={photo_id}&format=json&nojsoncallback=1'

        r = requests.get(url).json()
        print(r)

group_url = 'https://www.flickr.com/groups/velvia50/pool/'
group_id = get_group_id(group_url)
photo_ids = get_photo_ids(group_id)
photo_urls = get_photo_urls(photo_ids)