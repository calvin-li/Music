import os
import mutagen.id3


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


def rename_mp3(src, dst):
    os.rename(src, dst + ".mp3")


tags = {
    "Title": "TIT2",
    "Album": "TALB",
    "Picture": "APIC",
    "Genre": "TCON",
    "Artist": "TPE1",
    "Artist2": "TPE2",
    "Year": "TDRC"
}


def main():
    song_names = sorted(filter(lambda s: s.endswith("mp3"), os.listdir(".")))

    songs = []
    for name in song_names:
        songs.append(mutagen.id3.ID3(name))
        if name.__contains__('-'):
            spl = name.split('-')
            title_from_file = spl[0].strip()
            artist_from_file = spl[1].strip().strip(".mp3")
            title_from_song = str(songs[-1][tags["Title"]])
            artist_from_song = str(songs[-1][tags["Artist"]])

            if title_from_file != title_from_song:
                choice = input("Title mismatch: " + title_from_file + ", " + title_from_song + ": ")
                if choice == '1':
                    set_title(songs[-1], title_from_file)
                elif choice == '2':
                    rename_mp3(name, title_from_song)
                else:
                    set_title(songs[-1], choice)
                    rename_mp3(songs[-1], choice)

            if artist_from_file != artist_from_song:
                choice = input("Artist mismatch: " + artist_from_file + ", " + artist_from_song + ": ")
                if choice == '1':
                    set_artist(songs[-1], artist_from_file)
                elif choice == '2':
                    rename_mp3(name, title_from_file)
                else:
                    set_artist(songs[-1], choice)

        # try:
        #     title = songs[-1][tags["title"]]
        # except KeyError:
        #     print("\t" + name)
        #     mutagen.id3.TIT2()
        #     songs[-1].add(mutagen.id3.TIT2(mutagen=3, text=name))
        #     songs[-1].save()


main()
