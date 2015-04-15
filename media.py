import webbrowser


class Movie():
    """
    This class provides a way to store movie related information
    """
    
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, movie_rating):
        """
        Inits Movie object

        Parameters:
        movie_title - Movie title
        movie_storyline - Storyline details
        poster_image - Image URL for poaster
        trailer_youtube - Youtube URL for trailer
        movie_rating - "G", "PG-13", "R"      
        """
        
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.rating = movie_rating
                   
    def show_trailer(self):
        """Run Trailer"""
        
        webbrowser.open(self.trailer_youtube_url)
