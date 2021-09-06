# musiccharts
A small python script to scrap (electronic) music charts into directories with csv files.

### Installation
1. Download [**MusicCharts**.exe](https://github.com/DustinScharf/musiccharts/releases/download/v1.0/MusicCharts.zip "Click to download")
2. Run **MusicCharts**.exe  

## How to use musiccharts?
### GUI Mode
Open a terminal in the directory you installed musiccharts to and type `python3 main.py 999`  

![This image shows the GUI of musiccharts](window.png "The GUI")

### CLI Mode
Everything is safed into the directory `HOME/MusicCharts`  

Open a terminal in the directory you installed musiccharts to and use one of the following commands.

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
