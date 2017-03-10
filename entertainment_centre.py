""" entertainment_centre.py:
        Entry point of the entertainment_centre application. Will generate
        the fresh_tomatoes webpage based on the data in the movies list and
        open it in a browser. This module can be customised to add additional
        movies to the webpage.
"""
import media
import fresh_tomatoes

# Create the Movie objects.
avatar = media.Movie("Avatar",
                     "A marine on an alien planet.",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

star_wars = media.Movie("Star Wars",
                        "Farm boy saves the universe.",
                        "https://upload.wikimedia.org/wikipedia/en/8/87/StarWarsMoviePoster1977.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=vZ734NWnAHA")

fargo = media.Movie("Fargo",
                    "Stupid people doing greedy and violent things.",
                    "https://upload.wikimedia.org/wikipedia/en/a/ac/Fargo.jpg",
                    "https://www.youtube.com/watch?v=h2tY82z3xXU")

back_to_the_future = media.Movie("Back To The Future",
            "Teenage boy and a scientist team up to save the future.",
            "https://upload.wikimedia.org/wikipedia/en/d/d2/Back_to_the_Future.jpg",  # NOQA
            "https://www.youtube.com/watch?v=qvsgGtivCgs")

anchorman = media.Movie("Anchorman: The Legend of Ron Burgundy",
            "Dimwitted man thinks he's a big deal.",
            "https://upload.wikimedia.org/wikipedia/en/6/64/Movie_poster_Anchorman_The_Legend_of_Ron_Burgundy.jpg",  # NOQA
            "https://www.youtube.com/watch?v=bMejzXmvXGs")

lost_in_translation = media.Movie("Lost In Translation",
            "Man and woman bond in a foreign land.",
            "https://upload.wikimedia.org/wikipedia/en/4/4c/Lost_in_Translation_poster.jpg",  # NOQA
            "https://www.youtube.com/watch?v=sU0oZsqeG_s")

# Form a list of Movie objects.
movies = [avatar, star_wars, fargo, back_to_the_future,
          anchorman, lost_in_translation]

# Open the webpage.
fresh_tomatoes.open_movies_page(movies)
