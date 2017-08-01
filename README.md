# OkanimeDownloader

![download](https://user-images.githubusercontent.com/12420351/28639919-96da7642-7252-11e7-90e5-9a52fbb10c82.png)


Scrape your favorite anime from [Okanime](http://okanime.com/) without any effort. OkanimeDownloader is a wrapper around youtube-dl to download anime from [Okanime](http://okanime.com/).

I made it to look & feel exactly like youtube-dl, so if you're a fan of youtube-dl, this simple project is made for you! This project still in beta. It lacks a lot of features and might contains some bugs as well. But for now, it "just works".

## Requirements
* [Python 3.x](https://www.python.org/downloads/)
* [pip](https://pip.pypa.io/en/stable/installing/)
* [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) (recommended) 

## Installation
First, make sure you have [Python 3.x](https://www.python.org/downloads/), [pip](https://pip.pypa.io/en/stable/installing/), and [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed on your machine.

Run the following in your command prompt to install:
1. `git clone https://github.com/MoHD20/OkanimeDownloader.git`
2. `cd OkanimeDownloader` 
3. `pip install -r requirements.txt`

## Usage
```
usage: Oknime.py [-h] [--version] [-F] [-f FORMAT] [--playlist-end NUMBER]
                 URL [URL ...]

optional arguments:
  -h, --help            show this help message and exit

General Options:
  URL                   Add at least one url to download
  --version             Print program version and exit

Video Format Options:
  -F, --list-formats    List all available formats of requested videos

Video Format Options:
  -f FORMAT, --format FORMAT
                        Video format code, see the "FORMAT SELECTION" for more info

Video Selection:
  --playlist-end NUMBER
                        Playlist video to end at (default is None)

```

## Examples:

### 1. How to download one episode?

```
$ python3 okanime.py http://okanime.com/animes/one-piece/episodes/one-piece-797
```

As simple as that! This will download the highest quality video available for that episode.

### 2. How to download the video in a specific format?

**Step 1:**

List the available formats

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

**Step 2:**

Put the format code of your choice after the `-format` argument

`$ python3 Oknime.py http://okanime.com/animes/one-piece/episodes/one-piece-797 --format 0`

### 3. How to download more than one episode?

`$ python3 Oknime.py http://okanime.com/animes/one-piece/episodes/one-piece-790 --playlist-end 797`

This will download episodes 790 to 797.

## TO-DO:

I'm not sure I'll be able to make these things, so If you're interested just dive in.

- [ ] Progress bar (By capturing and parsing the [output of youtube-dl](https://github.com/rg3/youtube-dl#embedding-youtube-dl) and using [tqdm](https://github.com/tqdm/tqdm))

- [ ] Async downloading (using [asyncio](https://docs.python.org/3/library/asyncio.html) or something that would make it possible to download a punch of episode at the same time)

- [ ] Download meta-data (from: AniDB.net, TheTVDB.com, TheMovieDB.org...etc)
- [ ] Download movies from Okanime
- [ ] Make it installable via PyPI(ie. pip install okanimedownloader)

### Disclaimer: 

This project isn't officialy connected to [Okanime](http://okanime.com/) by any means. If you really love anime and could get it legally, then you should do that. Gotta support the industry! :heart:
