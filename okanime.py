import logging
from bs4 import BeautifulSoup
from urllib.request import urlsplit
import argparse
import re
from youtube_dl import YoutubeDL
import os
import sys
import requests
import json

__version__ = '0.1 BETA'

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(funcName)-5s %(message)s',
                    filename='OkanimeDownloader.log',
                    filemode='w')

console = logging.StreamHandler()
console.setLevel(logging.CRITICAL)
formatter = logging.Formatter('%(levelname)-8s : %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)


parser = argparse.ArgumentParser(description='Download from Okanime.')
general = parser.add_argument_group('General Options')
general.add_argument('URL', nargs='+', help='Add at least one url to download')
general.add_argument(
    '--version',
    action='version', version=__version__,
    help='Print program version and exit')

video_format = parser.add_argument_group('Video Format Options')
video_format.add_argument(
    '-F', '--list-formats',
    action='store_true', dest='listformats',
    help='List all available formats of requested videos')

video_format = parser.add_argument_group('Video Format Options')
video_format.add_argument(
    '-f', '--format',
    dest='format', metavar='FORMAT', default=None,
    help='Video format code, see the "FORMAT SELECTION" for all the info')

selection = parser.add_argument_group('Video Selection')
# selection.add_argument(
#     '--playlist-start',
#     dest='playliststart', metavar='NUMBER', default=None, type=int,
#     help='Playlist video to start at (default is %(default)s)')
selection.add_argument(
    '--playlist-end',
    dest='playlistend', metavar='NUMBER', default=None, type=int,
    help='Playlist video to end at (default is None)')

args = parser.parse_args()

logging.debug('Entered parameters: %s' % vars(args))


def get_Durl(general, args=None):
    """
    Determine the exact URL of the video to download
    """
    ### regex for supported downloading websites
    google_regex  = r'https?://(?:video\.google\.com/get_player\?.*?docid=|(?:docs|drive)\.google\.com/file/d/)([a-zA-Z0-9_-]{28,})'
    okanime_regex = r'https?://(?:cdn\d.okanime.com/v/)(?:[a-zA-Z0-9_-]){14,}'
    dailymo_regex = r'https?://(?:www.dailymotion.com/embed/video/)(?:[a-zA-Z0-9_-]){7,}'
    streama_regex = r'https?://(?:www)?streamango.com/embed(?:/embed)?/[a-zA-Z0-9_-]{16,}.*'
    tune_pk_regex = r'https?://(?:www)?embed.tune.pk/play/[a-zA-Z0-9_-]{7,}.*'
    rapidvi_regex = r'https?://(?:www)?.rapidvideo.com/e/[a-zA-Z0-9_-].*'

    if isinstance(general, list):
        general = general[0]

    okanime = requests.get(general)
    parse = BeautifulSoup(okanime.text, "html5lib")

    dic = {}
    for x in parse.find_all('a', {'class': 'load_player_episode'}):
        dic[x.get_text()] = 'http://okanime.com{}'.format(x['href'])
    logging.debug('availabe Jsons to scrape: {}'.format(dic))

    for key in dic.keys():
        temp = json.loads(requests.get(dic[key]).text)
        dic[key] = temp.get('url')
        logging.debug('found a punch of urls to download from: {} '.format(dic))
        if any(re.match(regex, dic[key]) for regex
               in [google_regex, okanime_regex, dailymo_regex, streama_regex, tune_pk_regex, rapidvi_regex]):
            logging.info('Found a video url {}'.format(dic[key]))
            try:
                download(dic[key], args=args)
                break
            except Exception as e:
                print("can't download from this URL: {}".format(dic[key]))
                logging.debug('url is not working {}'.format(dic[key]))
                continue



def my_hook(d):
    """
    funcetion for the post procedures that happen to the downloaded files after youtube-dl done its magic (ie. renaming)
    """
    episode, anime_name = current_anime_eps(args.URL)

    if d['status'] == 'finished':
        print('Done downloading, now renaming & moving ...')
        filename, extension = os.path.splitext(d['filename'])
        dirname = os.path.dirname(os.path.abspath(__file__))
        os.rename(os.path.join(dirname, d['filename']), os.path.join(dirname, anime_name + ' ' + episode.lstrip('0') + extension)) #/Users/hamza/Dropbox/My Py Projects/Okanime/[OKanime.com] OxP  (004).mkv-0ByGlIFp6qxNYSFZvLWQxR1RDd0k.mp4




def download(links, args=None):
    """
    download the actual video using youtube-dl
    """
    default = {'progress_hooks': [my_hook]}
    if args is not None:
        default.update(args)

    logging.debug('youtube-dl final arguments: {}'.format(default))

    with YoutubeDL(default) as ydl:
        logging.debug('url: {} ... trying scraping it '.format(links))
        ydl.download([links])


def current_anime_eps(url):
    """
    Determine the Anime's name and episode 
    """
    if isinstance(url, list):
        url = url[0]
    path = urlsplit(url).path
    episode = re.search(r'(\d{3})', path).group()
    anime_name = path.split('/')[2]
    return episode, anime_name


def next_episode(url):
    """
    Determine the next Episode of the Anime
    """

    if isinstance(url, list):
        url = url[0]

    episode, anime_name = current_anime_eps(url)
    episode = int(episode) + 1
    args.URL = 'http://okanime.com/animes/{}/episodes/{}-{numb:0=3d}'.format(anime_name, anime_name, numb=episode)
    logging.DEBUG('next episode URL:  {}'.format(args.URL))
    return get_Durl(args.URL)


def main():

    episode, name = current_anime_eps(args.URL)
    if len(args.URL) != 1:
        logging.critical('please enter just one url to download. you entered {} which are: {}'.format(len(args.URL), args.URL))
        sys.exit()

    if args.playlistend:
        get_Durl(args.URL)

        for _ in range(int(episode), int(args.playlistend)+1):
            next_episode(args.URL)

    elif args.listformats:
        get_Durl(args.URL, {'listformats': args.listformats})

    elif args.format:
        get_Durl(args.URL, {'format': args.format})

    else:
        get_Durl(args.URL)


if '__name__' == main():
    main()














