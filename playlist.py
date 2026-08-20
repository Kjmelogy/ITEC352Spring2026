# playlist.py (starter)
playlist = ["Here Comes the Sun", "Blue in Green", "All of Me"]

# Adds a song to the playlist
def add_song(title):
    """Add title to the global playlist. (No return)"""
    playlist.append(title)

# Removes a song from the playlist
def remove_song(title):
    """Remove first matching title from playlist.
    Returns True if removed, False if not found.
    """
    if title in playlist:
        playlist.remove(title)
        return True
    return False

# Finds a song in the playlist
def find_song(title):
    """Return index of first matching title, or -1 if not found."""
    if title in playlist:
        return playlist.index(title)
    return -1

# Makes a copy of the playlist
def get_playlist_copy():
    """Return a shallow copy of the playlist."""
    return playlist.copy()

# replaces a song in the playlist
def replace_song(old, new):
    """Replace first occurrence of old with new.
    Return (index, new) if replaced, else None.
    """
    # Song not found 
    idx = find_song(old)
    if idx == -1:
        return None
    # Add new song in place of old
    playlist[idx] = new
    return (idx, new)

# Runs the program
def main():
    #Prints the initial playlist
    print("Initial playlist:", playlist)

    #Adds a song
    # Function with no return value
    add_song("Dream a Little Dream")
    print("After add:", playlist)

    # Removes a song
    # Function with return value
    removed = remove_song("All of Me")
    print("Removed 'All of Me'?", removed)

    # Finds a song
    index = find_song("Blue in Green")
    print("Index of 'Blue in Green':", index)

    # Makes a copy of the playlist
    playlist_copy = get_playlist_copy()
    print("Copy of playlist:", playlist_copy)

    # Replaces a song in the playlist
    result = replace_song("Here Comes the Sun", "Here Comes the Night")
    print("Replace result:", result)
    print("Final playlist:", playlist)

if __name__ == "__main__":
    main()
