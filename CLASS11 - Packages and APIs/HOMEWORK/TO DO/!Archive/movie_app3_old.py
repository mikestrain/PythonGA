
import os
os.system("clear")
#Mike Strain, 2019-12-05 Python Class #2
search_or_ratings = 2
default_movie_list = ["Back to the Future", "Blade", "Spirited Away"]


class Movie(object):
    #movie data is a dictionary of movie data

    def __init__(self, movie_data):
        self.movie_data = movie_data

    def get_movie_title(self):
        """ Getter function that returns the value of the Title key in the movie_data dictionary."""
        return self.movie_data["title"]

    def get_movie_rating(self):
        """ Getter function that returns the value of the Rating key in the movie_data dictionary."""
        return self.movie_data["rating"]


def main(): 
    """ This is the main function.
    It does some things. """
    printAllRatings(default_movie_list)
    if search_or_ratings == 1:
        listSearchResults(default_movie_list)
    elif search_or_ratings == 2:
        printSingleMovieRating("Moana")
    else:
        print("Error! Your input must be equal to 1 or 2.")


#used in "if" statement
def listSearchResults(movieTitles): 
    """ Lists the search results for us. """
    for movie in movieTitles:
        print("\t",movie)

#used in "else" statement
def printSingleMovieRating(movie_query): 
    """ This function prints the rating for a specific movie. """

    myMovie = return_single_movie_object(movie_query,4)

    print(r"The rating for " + myMovie.get_movie_title() + " is " + str(myMovie.get_movie_rating()))

#used by default in the main function
def printAllRatings(movieList): 
    """ This prints all the movie ratings in a for loop. """
    for movie in movieList:
        movie_object = return_single_movie_object(movie, 4)
        print("The movie", movie_object.get_movie_title(), "has a rating of", movie_object.get_movie_rating())

#CREATES MOVIE OBJECTS WITH A TITLE AND A RATING
def return_single_movie_object(movie_title, movie_rating):
    movie_data = {"title":movie_title,"rating":movie_rating}
    myMovie = Movie(movie_data)
    return myMovie

if __name__ == "__main__":
    main()

# main.__doc__
# help(main)