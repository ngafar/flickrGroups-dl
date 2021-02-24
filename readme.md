# flickrGroups-dl

While the name Flickr may encourage feelings of nastolgia, the site is still alive. This project is a command line tool that helps users bulk download images from Flickr groups.

Why? Flick has a trove of images that have been uploaded of the years, and it's groups have curated these images in facinating ways. Examples include "subject" based groups (portraits, cats, lighthouses), as well as "technical" groups (photos take with a specific camera, or film stock).

These groups make it easy for users to create their own datasets easily.

## Installation 

Simply clone this repository as you would normally do:

```
git clone https://github.com/ngafar/flickrGroups-dl.git
cd flickrGroups-dl
```

From there install the project dependencies:

```
virtualenv env 
pip install -r requirements.txt
```

Then to run the program:

```
python main.py
```

** HOLD UP! ** Before you can use the program you have to add your API key. Keep reading to see how.

## Setup

You'll need an API key from Flickr. [Get one here](https://www.flickr.com/services/), it's free.

Once you have an API key, paste it into `secrets-sample.py`.
