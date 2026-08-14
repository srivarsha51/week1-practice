songs = [
    "Song A",
    "Song B",
    "Song C",
    "Song D",
    "Song E",
    "Song F",
    "Song G",
    "Song H"
]

# Display playlist slices
print("Complete Playlist:")
print(songs)

print("\nFirst 3 Songs:")
print(songs[:3])

print("\nLast 3 Songs:")
print(songs[-3:])

print("\nSongs from Position 3 to 6:")
print(songs[2:6])

print("\nEvery Alternate Song:")
print(songs[::2])

print("\nPlaylist in Reverse Order:")
print(songs[::-1])

print("\nPlaylist Without First and Last Song:")
print(songs[1:-1])


# Create short playlist
short_playlist = songs[2:6]

# Change one song in short_playlist
short_playlist[1] = "New Song"

# Display both playlists
print("\nOriginal Playlist:")
print(songs)

print("\nShort Playlist:")
print(short_playlist)