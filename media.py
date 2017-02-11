import webbrowser

class Movie():
    """
    Movie Class
    attributes:
        title
        storyline
        poster_image_url
        trailer_youtube_url
    functions:
        show_trailer
    """
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube


    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)