from objects_melogy import Movie

# Create two Movie objects
movie1 = Movie("The Dark Knight", "Action", 9)
movie2 = Movie("Shrek", "Comedy", 8)

# Display information about the movies
movie1.display_info()
print()

movie2.display_info()
print()

# Change the rating of the first movie
movie1.update_rating(10)