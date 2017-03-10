import webbrowser


class Movie():
    ''' This class provides a way to store movie related information.

        Attributes:
            title (str): The movie title.
            storyline (str): A brief movie synopsis.
            poster_image_url (str): The URL of the movie's poster image.
            trailer_youtube_url (str): The URL of the movie's trailer on
                                       youtube.
    '''

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        """ Class initialisation method """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """ Open the trailer of this movie in a web browser window. """
        webbrowser.open(self.trailer)
