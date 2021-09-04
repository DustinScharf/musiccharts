import sys

from musiccharts import genres
from musiccharts.MusicCharts import MusicCharts

if __name__ == '__main__':
    if len(sys.argv) != 2 or not sys.argv[1].isnumeric():
        print("This is only a test version.")
        print("Little Error, but here is the fix:")
        print()
        print("Use >>> python3 main.py 0")
        print("To get the Top 100 of all genres into the directory HOME/MusicCharts")
        print()
        print("Use >>> python3 main.py GENRE_ID")
        print("To get the Top 100 of a specific GENRE_ID into the directory HOME/MusicCharts")
        print("example: >>> python3 main.py 1")
        print("View all genre ids on https://github.com/DustinScharf/musiccharts (README.md)")
        print()
        print("Any other syntax causes this error")
        exit(1)

    music_charts = MusicCharts()
    genre_id = int(sys.argv[1])
    if genre_id == 0:
        music_charts.all_top_100_to_csv()
    else:
        music_charts.top_100(genre_id).to_csv_file()

    print("CSV put into HOME/MusicCharts : DONE")
