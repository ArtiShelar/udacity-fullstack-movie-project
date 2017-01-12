import webbrowser


# MyMovie class will create an object containing :
# 1. movie_id           this will be useful in case other features from
#                       TMDb are to be implemented
# 2. movie_title        this will contain the title of the movie
# 3. movie_storyline    this will contain the overview of the movie
# 4. movie_poster       this will contain the URL to the movie poster
# 5. movie_trailer      this will contain the URL to the trailer on YouTube
class MyMovie:

    def __init__(self, movie_id, movie_title, movie_storyline,
                 movie_poster, movie_trailer):
        self.id = movie_id  # movie_id may be required in the future
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_url = movie_poster
        self.trailer_url = movie_trailer

    def play_trailer(self):
        webbrowser.open(self.trailer_url)
