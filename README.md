# musiccharts
A small python script to scrap (electronic) music charts into directories with csv files.

## Installation
Download the files and run the commands below in the directory with the downloaded files.
<br />
Or run the command `pip install git+https://github.com/DustinScharf/musiccharts` in your terminal.

## How to use musiccharts?
Everything is safed into the directory HOME/MusicCharts  

Get TOP 100 of ALL GENRES: `python3 main.py 0`  
Get TOP 100 of GENRE with GENRE_ID: `python3 main.py GENRE_ID`  
_(see GENRE IDs below)_

**Example**  
Use `python3 main.py 1` to get the Top 100 drum and bass charts

### GENRE IDs
```
DRUM_AND_BASS = 1
HARD_TECHNO = 2
ELECTRONICA = 3

HOUSE = 5
TECHNO = 6
TRANCE = 7
HARD_DANCE_AND_HARDCODE = 8
BREAKS_AND_BREAKBEAT_AND_UK_BASS = 9

TECH_HOUSE = 11
DEEP_HOUSE = 12
PSY_TRANCE = 13
MINIMAL_AND_DEEP_TECH = 14
PROGRESSIVE_HOUSE = 15
DJ_TOOLS = 16

DUBSTEP = 18
```
