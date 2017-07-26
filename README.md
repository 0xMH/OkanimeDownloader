# OkanimeDownloader

![download](https://user-images.githubusercontent.com/12420351/28639919-96da7642-7252-11e7-90e5-9a52fbb10c82.png)


Scrape your favorite Anime from [Okanime](http://okanime.com/) with no effort. OkanimeDownloader is kind of a wrapper around youtube-dl to make it able to donwload from [Okanime](http://okanime.com/).

I made it to look & feel exactly like youtube-dl, so if you're a fan of youtube-dl, this simple project is made for you! 
This project still in Beta Release, It lacks a lot of features and possible contains some bugs too, but for now It's "just work"

## Requirements
* [Python 3.x](https://www.python.org/downloads/)
* [pip](https://pip.pypa.io/en/stable/installing/)
* [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) (recommended) 

## Installation
First, make sure you have [Python 3.x](https://www.python.org/downloads/), [pip](https://pip.pypa.io/en/stable/installing/), and [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed on your machine.
Run the following in your command prompt to install:

1. `git clone https://github.com/MoHD20/OkanimeDownloader.git`
2. `cd OkanimeDownloader` 
2. `pip install -r requirements.txt`

## Usage
```
usage: Oknime.py [-h] [--version] [-F] [-f FORMAT] [--playlist-end NUMBER]
                 URL [URL ...]

Download from Okanime.

optional arguments:
  -h, --help            show this help message and exit

General Options:
  URL                   Add at least one url to download
  --version             Print program version and exit

Video Format Options:
  -F, --list-formats    List all available formats of requested videos

Video Format Options:
  -f FORMAT, --format FORMAT
                        Video format code, see the "FORMAT SELECTION" for all
                        the info

Video Selection:
  --playlist-end NUMBER
                        Playlist video to end at (default is None)

```

### Examples:
`$ python3 okanime.py http://okanime.com/animes/one-piece/episodes/one-piece-797`

as simple as that, you will get the hightest quality possible from this Episode in you Disk!

but, what if you want a specific Format?

**first:**

you should list available Formats

```
$ python3 Oknime.py http://okanime.com/animes/one-piece/episodes/one-piece-797 --list-formats
[generic] FHLWGAJEB3?autostart=true: Requesting header
WARNING: Falling back on generic information extractor.
[generic] FHLWGAJEB3?autostart=true: Downloading webpage
[generic] FHLWGAJEB3?autostart=true: Extracting information
[info] Available formats for FHLWGAJEB3?autostart=true:
format code  extension  resolution note
0            mp4        480p       
1            mp4        720p       (best)
```

**second:**

choose the format you prefer then put Its format code after `-format` arguments

`$ python3 Oknime.py http://okanime.com/animes/one-piece/episodes/one-piece-797 --format 0`

### Disclaimer: 

This project Isn't officialy connected to [Okanime](http://okanime.com/) by any mean. If you really love Anime and could get it legally, then you should do that! gotta support the industry you know.
