
import os
os.system("clear")
#Mike Strain, 2019-12-05 Python Class #2
search_or_ratings = 2
my_source = "Hard Coded"
default_movie_list = ["Back to the Future", "Blade", "Spirited Away"]


class Movie(object):
    #movie data is a dictionary of movie data

    def __init__(self, movie_data):
        self.movie_data = movie_data

    def get_movie_title(self):
        """ Getter function that returns the value of the Title key in the movie_data dictionary."""
        return self.movie_data["Title"]

    def get_movie_rating(self,source="Hard Coded"):
        # print("\n\n")
        # print(source)

        """ Getter function that returns the value of the Rating key in the movie_data dictionary."""
        for rating_dictionary in self.movie_data["Rating"]:
            # print(rating_dictionary)
            if rating_dictionary["Source"] == source: 
                return rating_dictionary["Value"]
        return "--Wait -- The rating for {0} was not found".format(source)



def main(): 
    """ This is the main function.
    It does some things. """
    print("___Default Function___")
    printAllRatings(default_movie_list, my_source)

    print("\n___User Selection___")
    while True:
        if search_or_ratings == 1:
            listSearchResults(default_movie_list)
            break
        elif search_or_ratings == 2:
            printSingleMovieRating("Moana", my_source)
            break
        else:
            print("Error! Your input must be equal to 1 or 2.")




#used in "if" statement
def listSearchResults(movieTitles): 
    """ Lists the search results for us. """
    for movie in movieTitles:
        print("\t",movie)

#used in "else" statement
def printSingleMovieRating(movie_query,source="Hard Coded"): 
    """ This function prints the rating for a specific movie. """

    myMovie = return_single_movie_object(movie_query,4)

    print("""The rating for "{0}" is {1}""".format(myMovie.get_movie_title(),str(myMovie.get_movie_rating(source)))) #using triple quotes for literal evaluation of string.

#used by default in the main function
def printAllRatings(movieList,source="Hard Coded"): 
    """ This prints all the movie ratings in a for loop. """
    for movie in movieList:
        movie_object = return_single_movie_object(movie, 4)
        print("""The movie "{0}" has a rating of {1}""".format(movie_object.get_movie_title(),movie_object.get_movie_rating(source)))

#CREATES MOVIE OBJECTS WITH A TITLE AND A RATING
def return_single_movie_object(movie_title, movie_rating):

    ratings_list = [{"Source":"Hard Coded","Value":movie_rating}]

    movie_data = {"Title":movie_title,"Rating":ratings_list}
    myMovie = Movie(movie_data)

    return myMovie

if __name__ == "__main__":
    main()

# main.__doc__
# help(main)