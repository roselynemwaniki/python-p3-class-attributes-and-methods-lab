class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.count += 1
        
        # Update genre count
        if genre not in Song.genre_count:
            Song.genre_count[genre] = 0
        Song.genre_count[genre] += 1
        
        # Update artist count
        if artist not in Song.artist_count:
            Song.artist_count[artist] = 0
        Song.artist_count[artist] += 1
        
        # Track unique genres and artists
        if genre not in Song.genres:
            Song.genres.append(genre)
        if artist not in Song.artists:
            Song.artists.append(artist)

          