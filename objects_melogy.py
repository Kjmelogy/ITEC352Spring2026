class Movie:
    # Constructor
    def __init__(self, title, genre, rating):
        self.title = title
        self.genre = genre
        self.rating = rating

    # Displays the movie information
    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Genre: {self.genre}")
        print(f"Rating: {self.rating}/10")

    # Changes the movie rating
    def update_rating(self, new_rating):
        self.rating = new_rating
        print(f"{self.title}'s new rating is {self.rating}/10")