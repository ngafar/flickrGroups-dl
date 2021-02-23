# flickrGroups-dl
---
While the name Flickr may encourage feelings of nastolgia, the site is still alive. This project is a command line tool that helps users bulk download images from Flickr groups.

Why? Flick has a trove of images that have been uploaded of the years, and it's groups have curated these images in facinating ways. Examples include "subject" based groups (portraits, cats, lighthouses), as well as "technical" groups (photos take with a specific camera, or film stock).

These groups make it easy for users to create their own datasets easily.

## Installation 
---
Simply clone this repository as you would normally do:

```
git clone https://github.com/ngafar/flickrGroups-dl.git
cd flickrGroups-dl
```

From there install the project dependencies:

```
virtualenv env # create a virtual enviornment
pip install -r requirements.txt
```

Then to run the program:

```
python main.py
```