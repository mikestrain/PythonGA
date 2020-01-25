
class Movie(object):
    #Mike Strain, 2019-12-05 Python Class #2
    movie_title = "Back to the Future"
    movie_ratings = 8
    search_or_ratings = 3

    #movie data is a dictionary of movie data

    def __init__(self, movie_data):
        self.movie_data = movie_data

    def get_movie_title():
        """ Getter function that returns the value of the Title key in the movie_data dictionary."""

    def get_movie_rating():
        """ Getter function that returns the value of the Rating key in the movie_data dictionary."""


    def listSearchResults(movieTitles): 
        """ Lists the search results for us. """
        for movie in movieTitles:
            print("\t",movie)

      #used in "else" statement
    def printSingleMovieRating(): 
        """ This function prints the rating for a specific movie. """
        print(r"The rating for " + movie_title + " is " + str(movie_ratings))

    #used by default in the main function
    def printAllRatings(movieList): 
        """ This prints all the movie ratings in a for loop. """
        for movie in movieList:
            print("The movie", movie, "has a great rating!")

    def main(): 
        """ This is the main function.
        It does some things. """
        default_movie_list = ["Back to the Future", "Blade", "Spirited Away"]
        printAllRatings(default_movie_list)
        if search_or_ratings == 1:
            listSearchResults(default_movie_list)
        elif search_or_ratings == 2:
            printMovieRating()
        else:
            printSingleMovieRating()

    if __name__ == "__main__":
        main()

    main.__doc__
    help(main)