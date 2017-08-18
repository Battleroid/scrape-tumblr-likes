# scrape-tumblr-likes

Scrape Tumblr likes to specified directory. Create a `conf.py` containing a client all setup (that's referenced in [liked.py](liked.py)). Got tired of finding something to do this.

It's not perfect, and I have no intention of making it perfect, I just want to not have to make this again.

## requirements

* Python 2.7.x
* pytumblr (`pip install pytumblr`)

## usage

First (and only) argument is for the output directory. Defaults to current directory if none specified.

```bash
$ python liked.py /path/to/directory
> Output: /path/to/directory
> Page 1/31
Saving tumblr_ ... _400.gif
Saving tumblr_ ... _400.gif
Saving tumblr_ ... _1280.jpg
Saving tumblr_ ... _1280.jpg
Saving tumblr_ ... _1280.jpg
Saving tumblr_ ... _1280.jpg
```
