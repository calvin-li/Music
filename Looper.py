import os
import mutagen.id3
import re


def isascii(string):
    try:
        string.encode('ascii')
    except UnicodeEncodeError:
        return False
    return True


def set_title(song, new_title):
    song.add(mutagen.id3.TIT2(mutagen=3, text=new_title))
    song.save()


def set_artist(song, artists):
    artists = artists.replace("；", ";")
    song.add(mutagen.id3.TPE1(mutagen=3, text=artists))
    song.save()


def set_comment(song, comment):
    song.add(mutagen.id3.COMM(mutagen=3, text=comment))
    song.save()


def rename_mp3(src, dst):
    os.rename(src, dst.strip().replace(".mp3", "") + ".mp3")


tags = {
    "Title": "TIT2",
    "Album": "TALB",
    "Picture": "APIC",
    "Genre": "TCON",
    "Artist": "TPE1",
    "Artist2": "TPE2",
    "Year": "TDRC",
    "Comments": "COMM::XXX"
}


def main():
    song_names = sorted(filter(lambda s: s.endswith("mp3"), os.listdir(".")))

    songs = []
    for name in song_names:
        song = mutagen.id3.ID3(name)
        songs.append(song)

        title = str(song[tags["Title"]])
        artist = str(song[tags["Artist"]])

        if title.__contains__("齣頭天"):
            title = "出頭天"
            set_title(song, title)
            rename_mp3(name, title + " - " + artist)


main()
