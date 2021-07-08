import sys

from musiccharts.MusicCharts import MusicCharts

if __name__ == '__main__':
    # print("This is the name of the script: ", sys.argv[0])
    # print("Number of arguments: ", len(sys.argv))
    # print("The arguments are: ", str(sys.argv))

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
        print("DRUM_AND_BASS = 1 | HARD_TECHNO = 2 | ELECTRONICA = 3\n"
              "\n"
              "HOUSE = 5 | TECHNO = 6 | TRANCE = 7\n"
              "HARD_DANCE_AND_HARDCODE = 8\n"
              "BREAKS_AND_BREAKBEAT_AND_UK_BASS = 9\n"
              "\n"
              "TECH_HOUSE = 11 | DEEP_HOUSE = 12 | PSY_TRANCE = 13 | MINIMAL_AND_DEEP_TECH = 14\n"
              "PROGRESSIVE_HOUSE = 15 | DJ_TOOLS = 16 | # ELECTRO_HOUSE = 17 | DUBSTEP = 18")
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
