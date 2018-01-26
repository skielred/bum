# 🎵 bum

[![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE.md)
[![Build Status](https://travis-ci.org/dylanaraps/bum.svg?branch=master)](https://travis-ci.org/dylanaraps/bum)
[![Donate](https://img.shields.io/badge/donate-patreon-yellow.svg)](https://www.patreon.com/dyla)

## About this fork

This fork is based on the `players` branch (`22d820c`) from the original `bum` package.

It fixes the import of `players` module to use `bum` with more music players when installing with a Python packages manager.

It prioritizes the detection of `cmus` over `mpd`. This is strictly due to my personal usage. Sometimes I have the `mpd` daemon running even when `cmus` is opened. In these cases, I'm obviously listening music from `cmus`, so I changed the detection order.

It changes the default album art picture size from 250 to 1000 pixels. Also based on personal usage. I could not get a non-blurred picture with the 250 pixels resolution (maybe because I use `i3`?).

This version is based on `bum-0.1.2` and is named `bum-0.1.2-skiel`.

To install this fork using `PyPI`, run:

```sh
pip install --user git+"https://github.com/skielred/bum"
```
to install locally. Replace `pip` with `pip3` or `pip3.6` based on your configuration. This package requires Python 3.6+.


# Original README

`bum` is a daemon that downloads album art for songs playing and displays them in a little window. `bum` doesn't loop on a timer, instead it waits for a `SIGUSR1` signal. When it receives `SIGUSR1` it wakes up and downloads album art for the current playing track. This makes `bum` lightweight and makes it idle at `~0%` CPU usage.

`bum` uses [musicbrainz](https://musicbrainz.org/) to source and download cover art, if an album is missing it's cover art you can easily create an account and fill in the data yourself. `bum` outputs a `release-id` which you can use to find the exact entry on musicbrainz.

Note: `bum` is meant to be used with files that don't have embedded album art (`mopidy-spotify`).


![showcase](http://i.imgur.com/uKomDoL.gif)


## Dependencies

- `python 3.6+`
- `python-mpv`
- `musicbrainzngs`

**Player Dependencies**

- `cmus`: `pycmus`
- `mpd`/`mopidy`: `python-mpd2`
- `dbus players`: `playerctl`, `pygobject`


## Installation

```sh
pip3 install --user bum
```


## Usage

```sh
usage: bum [-h] [--size "px"] [--cache_dir "/path/to/dir"] [--version]

bum - Download and display album art for mpd tracks.

optional arguments:
  -h, --help            show this help message and exit
  --size "px"           what size to display the album art in.
  --cache_dir "/path/to/dir"
                        Where to store the downloaded cover art.
  --version             Print "bum" version.
  --port                Use a custom mpd port.
```


## Donate

Donations will allow me to spend more time working on `bum`.

If you like `bum` and want to give back in some way you can donate here:

**https://patreon.com/dyla**
