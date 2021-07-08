# musiccharts
A small python script to scrap (electronic) music charts into directories with csv files.

## install
simply download the files and run the commands above in the directory with the downloaded files
<br />
or
<br />
`pip install git+https://github.com/DustinScharf/musiccharts`

## current possible
use `python3 main.py 0` to get the Top 100 of all genres into the directory HOME/MusicCharts
<br /><br />
use `python3 main.py GENRE_ID` to get the Top 100 of a specific GENRE_ID into the directory HOME/MusicCharts
<br />
example: `python3 main.py 1` to get the Top 100 drum and bass charts into the directory HOME/MusicCharts

### genre ids
```DRUM_AND_BASS = 1
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

DUBSTEP = 18```
