from __future__ import print_function
from conf import client
import requests
import sys
import os

# TODO: maybe someday, if I'm not feeling lazy, I would use asyncio to speed this up


def fetch_post(post, path):
    if 'photos' in post:
        for image in post[unicode('photos', 'utf-8')]:
            url = image[unicode('original_size', 'utf-8')][unicode(
                'url', 'utf-8')]
            filename = url.split('/')[-1]
            fpath = os.path.join(path, filename)
            r = requests.get(url)
            if not os.path.exists(fpath):
                print('Saving {}'.format(filename))
                with open(fpath, 'wb') as f:
                    f.write(r.content)
            else:
                print('* skipping {}'.format(filename))


def main(path):
    total_liked = int(client.likes()[unicode('liked_count', 'utf-8')])
    for offset in range(0, total_liked, 50):
        print('> Page {}/{}'.format((offset / 50) + 1, int(total_liked / 50)))
        posts = client.likes(offset=offset, limit=50)['liked_posts']
        for post in posts:
            fetch_post(post, path)


if __name__ == '__main__':
    path = sys.argv[1] if len(sys.argv) > 0 else './'
    print('> Output: {}'.format(path))
    if not os.path.exists(path):
        os.mkdir(path)
    main(path)
