import mutagen
import mutagen.mp3
import mutagen.id3
import os

tags = {
    "title": "TIT2",
    "album": "TALB",
    "picture": "APIC",
    "Genre": "TCON",
    "Artist": "TPE1",
    "Artist2": "TPE2",
    "Year": "TDRC"
}

songNames = filter(lambda s: s.endswith("mp3"), os.listdir("."))
songNames.sort()

songs = []
for name in songNames:
    print name
    songs.append(mutagen.id3.ID3(name))
    try:
        print songs[-1][tags["title"]]
    except KeyError:
        mutagen.id3.TIT2()
        songs[-1].add(mutagen.id3.TIT2(mutagen=3, text=name))

