import requests
from secrets import API_KEY

def get_group_id(group_url):
    url = f'https://www.flickr.com/services/rest/?method=flickr.urls.lookupGroup&api_key={API_KEY}&url={group_url}&format=json&nojsoncallback=1'

    r = requests.get(url).json()
    group_id = (r['group']['id'])

    return group_id

group_url = 'https://www.flickr.com/groups/velvia50/pool/'
group_id = get_group_id(group_url)
print(group_id)